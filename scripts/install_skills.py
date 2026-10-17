#!/usr/bin/env python3
"""Selectively copy self-contained custom skills. Dry-run unless --apply is supplied."""
import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def install(name, destination, apply=False):
    known = {p.name for p in (ROOT/'skills').iterdir() if (p/'SKILL.md').is_file()}
    if name not in known:
        raise ValueError('Unknown custom skill; use --list')
    source = ROOT/'skills'/name
    target = Path(destination).expanduser().resolve()/name
    if target.exists():
        raise ValueError('Destination exists; no files were overwritten: '+str(target))
    if any(p.is_symlink() for p in source.rglob('*')):
        raise ValueError('Skill contains a symlink; inspect before installation')
    if apply:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)
    return {'skill': name, 'destination': str(target), 'copied': apply, 'mode': 'apply' if apply else 'dry-run'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--skill')
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        if args.list:
            print('\n'.join(sorted(p.name for p in (ROOT/'skills').iterdir() if (p/'SKILL.md').is_file())))
        elif args.skill and args.destination:
            print(json.dumps(install(args.skill, args.destination, args.apply), indent=2))
        else:
            parser.error('Supply --list or both --skill and --destination')
        return 0
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())

