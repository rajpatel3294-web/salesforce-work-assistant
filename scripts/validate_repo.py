#!/usr/bin/env python3
"""Structural validation, local links and lock/catalog consistency. No org validation."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    errors = []
    custom = json.loads((root/'catalog/custom-skills.json').read_text())
    cases = json.loads((root/'evals/scenarios.json').read_text())
    covered = {case['skill'] for case in cases}
    names = {item['name'] for item in custom}
    if len(names) != len(custom):
        errors.append('Duplicate custom catalog names')
    actual_names = {p.name for p in (root/'skills').iterdir() if p.is_dir()}
    if names != actual_names:
        errors.append('Custom catalog and skill directories differ')
    for item in custom:
        name = item['name']
        path = root/item['path']
        content = (path/'SKILL.md').read_text()
        if not re.fullmatch(r'[a-z0-9-]{1,64}', name):
            errors.append('Invalid skill name: '+name)
        if not content.startswith('---\nname: '+name+'\ndescription: '):
            errors.append('Invalid frontmatter: '+name)
        try:
            desc = json.loads(content.splitlines()[2].removeprefix('description: '))
            if not desc.strip():
                raise ValueError('empty description')
        except (ValueError, IndexError):
            errors.append('Invalid description: '+name)
        for required in ('## Workflow', 'references/runtime-contract.md', 'references/sources.md'):
            if required not in content:
                errors.append(name+': missing '+required)
        if name not in covered:
            errors.append(name+': no evaluation scenario')
        agent = path/'agents/openai.yaml'
        if not agent.exists() or '$'+name not in agent.read_text():
            errors.append(name+': missing/mismatched agent metadata')
    for path in root.rglob('*.md'):
        if '.git' in path.parts or 'vendor' in path.relative_to(root).parts:
            continue
        content = path.read_text()
        if '[TODO' in content:
            errors.append(str(path.relative_to(root))+': unfinished template')
        for link in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in link or link.startswith(('#', 'mailto:')):
                continue
            destination = (path.parent/link.split('#')[0]).resolve()
            if not destination.exists():
                errors.append(str(path.relative_to(root))+': broken local link '+link)
    lock = json.loads((root/'upstream.lock.json').read_text())
    upstream = json.loads((root/'catalog/upstream-skills.json').read_text())
    if len(upstream) != lock['skill_count'] or any(x['commit'] != lock['commit'] for x in upstream):
        errors.append('Upstream catalog differs from lockfile')
    vendor = root/lock['path']
    if not (vendor/'skills').is_dir():
        errors.append('Initialize upstream submodule before full validation')
    else:
        actual = subprocess.check_output(['git','-C',str(vendor),'rev-parse','HEAD'],text=True).strip()
        if actual != lock['commit']:
            errors.append('Upstream checkout differs from lockfile')
        state = subprocess.check_output(['git','-C',str(vendor),'status','--porcelain'],text=True).strip()
        if state:
            errors.append('Upstream submodule has local changes')
    return errors

if __name__ == '__main__':
    try:
        failures = validate()
        if failures:
            print('\n'.join('FAIL: '+x for x in failures))
            sys.exit(1)
        print('PASS: custom skills, agent metadata, evaluation coverage, local links and upstream lock/catalog')
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print('FAIL: '+str(exc))
        sys.exit(1)

