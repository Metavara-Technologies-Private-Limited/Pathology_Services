#!/usr/bin/env python3
"""Accept both sides for unmerged Git files by concatenating stage 2 and stage 3 blobs.

This script must be run from the repository root. It will:
- find unmerged files from `git ls-files -u`
- for each file, read stage 2 (ours) and stage 3 (theirs) blobs
- write combined content: stage2 + '\n' + stage3 into the working tree
- `git add` the file to mark as resolved
"""
import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def run(cmd):
    return subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True)

def get_unmerged_files():
    p = run('git ls-files -u')
    if p.returncode != 0:
        print('git ls-files -u failed:', p.stderr, file=sys.stderr)
        sys.exit(1)
    files = set()
    for line in p.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 4:
            path = parts[3]
            files.add(path)
    return sorted(files)

def read_blob(stage, path):
    p = run(f'git show :{stage}:{path}')
    if p.returncode != 0:
        return None
    return p.stdout

def main():
    files = get_unmerged_files()
    if not files:
        print('No unmerged files found.')
        return

    resolved = []
    for f in files:
        print('Processing', f)
        s2 = read_blob(2, f)
        s3 = read_blob(3, f)
        if s2 is None or s3 is None:
            print('  Skipping (missing stage blobs)')
            continue
        combined = s2
        if not combined.endswith('\n'):
            combined += '\n'
        combined += s3
        path = ROOT / f
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(combined, encoding='utf-8')
        add = run(f'git add "{f}"')
        if add.returncode == 0:
            resolved.append(f)
        else:
            print('  git add failed:', add.stderr)

    if resolved:
        print('Resolved and staged:')
        for r in resolved:
            print(' -', r)
    else:
        print('No files resolved.')

if __name__ == '__main__':
    main()
