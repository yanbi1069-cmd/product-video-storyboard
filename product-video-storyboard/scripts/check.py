"""Read-only structural checks; no API calls, writes or semantic image claims."""
import argparse
from pathlib import Path
import re
import struct
import sys


def check_skill(root):
    errors = []
    path = root / 'SKILL.md'
    if not path.is_file():
        return ['Missing SKILL.md']
    content = path.read_text(encoding='utf-8-sig')
    header = re.match(r'^---\n(.*?)\n---', content, re.S)
    if not header:
        return ['Missing YAML frontmatter']
    if not re.search(r'^name: product-video-storyboard$', header[1], re.M):
        errors.append('Unexpected skill name')
    if not re.search(r'^description: .+', header[1], re.M):
        errors.append('Missing description')
    for target in re.findall(r'\]\((references/[^)]+)\)', content):
        if not (root / target).is_file():
            errors.append('Missing reference: ' + target)
    for path in root.rglob('*'):
        if path.is_file() and (path.name.startswith('.env') or path.suffix == '.zip'):
            errors.append('Unexpected credential/archive file: ' + path.name)
    return errors


def check_output(root, text_only=False):
    errors = []
    prompt = root / 'prompt.txt'
    if not prompt.is_file():
        errors.append('Missing prompt.txt')
    else:
        text = prompt.read_text(encoding='utf-8-sig').rstrip('\r\n')
        if not text.strip():
            errors.append('Empty prompt')
        if '\n' in text or '\r' in text:
            errors.append('Prompt has embedded newline')
        if re.search(r'\[[^\]]+\]', text) or '```' in text:
            errors.append('Possible unfilled template slot or code fence')
    if text_only:
        if not (root / 'img.txt').is_file():
            errors.append('Missing text-only img.txt')
    else:
        image = root / 'sb.png'
        if not image.is_file():
            errors.append('Missing sb.png')
        else:
            with image.open('rb') as stream:
                head = stream.read(24)
            if len(head) < 24 or head[:8] != b'\x89PNG\r\n\x1a\n' or head[12:16] != b'IHDR':
                errors.append('Not a PNG with IHDR')
            else:
                width, height = struct.unpack('>II', head[16:24])
                if width <= 0 or height <= width:
                    errors.append('Storyboard must be portrait')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['skill', 'output'])
    parser.add_argument('folder', type=Path)
    parser.add_argument('--text-only', action='store_true')
    args = parser.parse_args()
    try:
        errors = (check_skill(args.folder) if args.mode == 'skill'
                  else check_output(args.folder, args.text_only))
    except (OSError, UnicodeError) as exc:
        errors = [str(exc)]
    for error in errors:
        print('FAIL: ' + error)
    if not errors:
        print('PASS: structural checks only; visual/semantic QA still required')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
