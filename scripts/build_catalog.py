#!/usr/bin/env python3
"""Regenerate the pinned upstream inventory. Requires PyYAML only for maintenance."""
import json
import subprocess
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

def main():
    base = ROOT/'vendor/sf-skills'
    lock = json.loads((ROOT/'upstream.lock.json').read_text())
    actual = subprocess.check_output(['git', '-C', str(base), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != lock['commit']:
        raise SystemExit('Upstream HEAD differs from lockfile; review update before regenerating')
    entries = []
    for p in sorted((base/'skills').glob('*/SKILL.md')):
        raw = p.read_text()
        data = yaml.safe_load(raw.split('---', 2)[1])
        meta = data.get('metadata', {}) or {}
        entries.append({'name': data['name'], 'description': data['description'],
                        'path': p.relative_to(ROOT).as_posix(),
                        'domains': meta.get('domains', []),
                        'cliTools': meta.get('cliTools', []), 'mcpTools': meta.get('mcpTools', {}),
                        'status': 'upstream-unvalidated', 'commit': actual})
    if len(entries) != lock['skill_count']:
        raise SystemExit('Skill count differs from lockfile; review update first')
    (ROOT/'catalog/upstream-skills.json').write_text(json.dumps(entries, indent=2)+'\n')
    custom = json.loads((ROOT/'catalog/custom-skills.json').read_text())
    lines = ['# Skill catalog', '', '## Custom workflows', '', '| Skill | Purpose |', '| --- | --- |']
    for item in custom:
        lines.append(f"| [{item['name']}](../{item['path']}/SKILL.md) | {item['description']} |")
    lines += ['', '## Pinned Salesforce foundation', '',
              f"{len(entries)} skills at `{actual}`. Listed is not the same as runtime validated.", '',
              'Tool requirements below are declared frontmatter, not a complete executable dependency audit.', '',
              '| Skill | Declared domains | Declared MCP dependency |', '| --- | --- | --- |']
    for item in entries:
        domains = ', '.join(item['domains'])
        mcp = ', '.join(item['mcpTools']) if isinstance(item['mcpTools'], dict) else str(item['mcpTools'])
        lines.append(f"| [{item['name']}](../{item['path']}) | {domains} | {mcp or 'Read skill for details'} |")
    (ROOT/'catalog/README.md').write_text('\n'.join(lines)+'\n')
    print(f'Indexed {len(custom)} custom and {len(entries)} upstream skills')

if __name__ == '__main__':
    main()

