#!/usr/bin/env python3
"""Resolve git merge conflict markers by accepting both sides.

Usage: run from the repository root. Backs up each modified file with a .orig extension.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def resolve_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8', errors='surrogateescape')
    if '<<<<<<<' not in text:
        return False

    out_lines = []
    i = 0
    lines = text.splitlines()
    changed = False
    while i < len(lines):
        line = lines[i]
        if line.startswith('<<<<<<<'):
            # find ======= and >>>>>>>
            i += 1
            a_lines = []
            while i < len(lines) and not lines[i].startswith('======='):
                a_lines.append(lines[i])
                i += 1
            if i >= len(lines):
                # malformed conflict, keep original
                out_lines.append(line)
                break
            # skip '======= '
            i += 1
            b_lines = []
            while i < len(lines) and not lines[i].startswith('>>>>>>>'):
                b_lines.append(lines[i])
                i += 1
            # skip '>>>>>>>'
            i += 1
            # accept both: A then B
            out_lines.extend(a_lines)
            out_lines.extend(b_lines)
            changed = True
        else:
            out_lines.append(line)
            i += 1

    if changed:
        backup = path.with_suffix(path.suffix + '.orig')
        if not backup.exists():
            path.replace(backup)
            # write resolved content to original path
            path.write_text('\n'.join(out_lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
        else:
            # backup already exists, just overwrite file
            path.write_text('\n'.join(out_lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
    return changed

def main():
    modified = []
    for p in ROOT.rglob('*'):
        if p.is_file():
            # skip virtual env and .git
            if any(part in ('env', '.venv', '.git', 'node_modules') for part in p.parts):
                continue
            try:
                if resolve_file(p):
                    modified.append(str(p.relative_to(ROOT)))
            except Exception as e:
                print(f'Error processing {p}: {e}', file=sys.stderr)

    if modified:
        print('Modified files:')
        for m in modified:
            print(' -', m)
    else:
        print('No merge conflict markers found.')

if __name__ == '__main__':
    main()
