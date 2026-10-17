#!/usr/bin/env python3
"""Report local capabilities without reading authentication or contacting any org."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def inspect():
    tools = {}
    for name in ('git', 'sf', 'node', 'npm', 'java', 'jq'):
        executable = shutil.which(name)
        tools[name] = {'available': bool(executable)}
        if executable and name in ('git', 'sf', 'node'):
            try:
                result = subprocess.run([executable, '--version'], capture_output=True,
                                        text=True, timeout=15, check=False)
                tools[name]['version'] = (result.stdout or result.stderr).strip().splitlines()[:1]
            except (OSError, subprocess.TimeoutExpired):
                tools[name]['version'] = ['version check unavailable']
    return {'python': sys.version.split()[0], 'python_supported': sys.version_info >= (3, 10),
            'upstream_initialized': (ROOT/'vendor/sf-skills/skills').is_dir(),
            'tools': tools, 'org_authentication': 'not inspected',
            'note': 'Availability does not establish authentication, product entitlement or runtime validation.'}

if __name__ == '__main__':
    result = inspect()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['python_supported'] else 1)

