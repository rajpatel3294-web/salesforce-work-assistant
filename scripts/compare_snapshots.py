#!/usr/bin/env python3
"""Compare metadata_snapshot JSON files without reading or mutating an org."""
import argparse
import json
import sys
from pathlib import Path

def compare(before, after):
    for value in (before, after):
        if value.get('schema_version') != 1 or not isinstance(value.get('files'), list):
            raise ValueError('Expected metadata snapshot schema version 1')
        if value.get('errors') or any(x.get('parse_error') for x in value['files']):
            raise ValueError('Snapshot contains parse errors; resolve them before comparison')
        paths = [x['path'] for x in value['files']]
        if len(paths) != len(set(paths)):
            raise ValueError('Duplicate paths in snapshot')
    old = {x['path']: x['sha256'] for x in before['files']}
    new = {x['path']: x['sha256'] for x in after['files']}
    return {'added': sorted(new.keys()-old.keys()), 'removed': sorted(old.keys()-new.keys()),
            'changed': sorted(k for k in old.keys() & new.keys() if old[k] != new[k]),
            'unchanged_count': sum(old[k] == new[k] for k in old.keys() & new.keys()),
            'interpretation': 'Byte-level differences only; review business semantics separately.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path)
    parser.add_argument('after', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(compare(json.loads(args.before.read_text()), json.loads(args.after.read_text())), indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())

