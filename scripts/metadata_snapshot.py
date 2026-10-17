#!/usr/bin/env python3
"""Read-only inventory of local Salesforce source. Never contacts Salesforce.

Output contains paths, hashes and selected metadata, not Apex bodies or field values.
Paths and metadata names may still be private. Store output outside version control.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

EXCLUDED = {'.git', '.sf', '.sfdx', '.venv', 'node_modules', 'artifacts', 'org-data', 'vendor'}
SUFFIXES = ('.cls', '.trigger', '.xml', '.js', '.ts', '.html', '.css')
NS = {'m': 'http://soap.sforce.com/2006/04/metadata'}

def snapshot(root):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError('Source must be an existing directory')
    records, errors = [], []
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if any(part in EXCLUDED for part in rel.parts) or path.is_symlink() or not path.is_file():
            continue
        if not path.name.endswith(SUFFIXES):
            continue
        if not path.resolve().is_relative_to(root):
            continue
        raw = path.read_bytes()
        item = {'path': rel.as_posix(), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
        if path.suffix == '.xml':
            try:
                if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper():
                    raise ValueError('DTD/entity declarations are not accepted')
                doc = ET.fromstring(raw)
                item['metadata_type'] = doc.tag.rsplit('}', 1)[-1]
                for key in ('apiVersion', 'status', 'processType', 'triggerOrder', 'active'):
                    node = doc.find('m:'+key, NS)
                    if node is not None:
                        item[key] = node.text
                if item['metadata_type'] == 'Flow':
                    item['object'] = doc.findtext('m:start/m:object', namespaces=NS)
                    item['trigger_type'] = doc.findtext('m:start/m:triggerType', namespaces=NS)
                    item['record_trigger_type'] = doc.findtext('m:start/m:recordTriggerType', namespaces=NS)
            except (ET.ParseError, ValueError) as exc:
                errors.append({'path': rel.as_posix(), 'error': str(exc)})
                item['parse_error'] = True
        records.append(item)
    return {'schema_version': 1, 'scope': 'local source only; file hashes are not semantic equivalence',
            'files': records, 'errors': errors}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    try:
        data = snapshot(args.source)
        text = json.dumps(data, indent=2)+'\n'
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text)
        else:
            print(text, end='')
        return 2 if data['errors'] else 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())

