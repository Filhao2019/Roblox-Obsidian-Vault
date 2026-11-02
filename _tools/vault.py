"""Local-only vault search, section reading and integrity checks. Python 3.10+."""
import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', '.obsidian', '.cache', '__pycache__', '_tools'}
VENDORED = '11 LihFolk V2'  # third-party CC BY import: searchable, not held to this vault's note rules
ADMIN = {'README.md', 'CHANGELOG.md', 'AGENTS.md', 'CLAUDE.md', 'LICENSE.md'}


def prose(text):
    """Exclude fenced examples and comments from navigational link checks."""
    text = re.sub(r'^(`{3,}|~{3,})[^\n]*\n.*?^\1[^\n]*$', '', text, flags=re.M | re.S)
    return re.sub(r'<!--.*?-->', '', text, flags=re.S)


def words(text):
    return re.findall(r'[a-z0-9]+', text.casefold())


def notes(root):
    result = []
    for path in sorted(root.rglob('*.md')):
        if any(part in EXCLUDED for part in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding='utf-8-sig')
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        metadata = {}
        if match:
            for line in match[1].splitlines():
                key, sep, value = line.partition(':')
                if sep:
                    metadata[key.strip()] = value.strip().strip('\"\'')
        body = text[match.end():] if match else text
        headings = re.findall(r'^#{1,6}\s+(.+?)\s*#*$', prose(body), re.M)
        summary = next((p.strip() for p in prose(body).split('\n\n')
                        if p.strip() and not p.lstrip().startswith(('#', '|', 'Links:', '>'))), '')
        result.append({'path': path.relative_to(root).as_posix(), 'title': path.stem,
                       'status': metadata.get('status', 'unspecified'), 'metadata': metadata,
                       'headings': headings, 'summary': re.sub(r'\s+', ' ', summary)[:320],
                       'body': body, 'text': text})
    return result


def search(root, query, limit=3):
    query_words = set(words(query))
    if not query_words:
        return []
    docs = notes(root)
    frequencies = Counter()
    indexed = []
    for doc in docs:
        fields = [(doc['title'], 9), (' '.join(doc['headings']), 3),
                  (doc['metadata'].get('tags', ''), 4), (prose(doc['body']), 1)]
        counts = Counter()
        for text, weight in fields:
            for word, count in Counter(words(text)).items():
                counts[word] += weight * min(count, 4)
        frequencies.update(counts.keys())
        indexed.append((doc, counts))
    hits = []
    for doc, counts in indexed:
        matched = query_words & counts.keys()
        if not matched:
            continue
        score = sum((1 + math.log1p(len(docs) / frequencies[w])) * counts[w] for w in matched)
        score *= len(matched) / len(query_words)
        if query.casefold() in doc['title'].casefold():
            score *= 2
        hits.append({key: doc[key] for key in ('path', 'title', 'status', 'summary', 'headings')} | {'score': round(score, 3)})
    return sorted(hits, key=lambda d: (-d['score'], d['path']))[:limit]


def read_section(root, title, heading=None):
    matches = [d for d in notes(root) if d['title'].casefold() == title.casefold()
               or d['path'].casefold() == title.casefold()]
    if len(matches) != 1:
        raise ValueError(f'Expected one exact note title or relative path; found {len(matches)}')
    doc = matches[0]
    text = doc['body']
    if heading:
        # Ignore heading-shaped text inside fenced examples.
        candidates = list(re.finditer(r'^(#{1,6})\s+(.+?)\s*#*$', text, re.M))
        fence = False
        real_offsets = set()
        offset = 0
        for line in text.splitlines(keepends=True):
            if re.match(r'^\s*(`{3,}|~{3,})', line):
                fence = not fence
            elif not fence and line.startswith('#'):
                real_offsets.add(offset)
            offset += len(line)
        candidates = [m for m in candidates if m.start() in real_offsets]
        found = [i for i, m in enumerate(candidates) if m[2].casefold() == heading.casefold()]
        if len(found) != 1:
            raise ValueError('Heading missing or ambiguous; use an exact heading from search output')
        i = found[0]
        start = candidates[i]
        end = next((m.start() for m in candidates[i+1:] if len(m[1]) <= len(start[1])), len(text))
        text = text[start.start():end]
    return f"{doc['path']} [status: {doc['status']}]\n\n{text.strip()}"


def check(root):
    errors = []
    docs = notes(root)
    targets = {}
    for path in root.rglob('*'):
        parts = path.relative_to(root).parts
        if not path.is_file() or any(p in EXCLUDED for p in parts) or parts[0] == VENDORED:
            continue
        rel = path.relative_to(root).as_posix()
        for key in {rel, path.name, rel[:-3] if path.suffix == '.md' else rel,
                    path.stem if path.suffix == '.md' else path.name}:
            targets.setdefault(key, set()).add(rel)
    for doc in docs:
        path = doc['path']
        if path.startswith(VENDORED + '/'):
            continue
        if Path(path).name not in ADMIN:
            meta = doc['metadata']
            for field in ('title', 'date', 'tags', 'status'):
                if not meta.get(field):
                    errors.append(f'{path}: missing {field}')
            if meta.get('status') not in {'stub', 'researched', 'untested', 'verified'}:
                errors.append(f'{path}: invalid status')
            if not path.startswith('_Templates/') and meta.get('title') != doc['title']:
                errors.append(f'{path}: title does not match filename')
            if not path.startswith('_Templates/') and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', meta.get('date', '')):
                errors.append(f'{path}: date must use YYYY-MM-DD')
        navigable = re.sub(r'`[^`\n]*`', '', prose(doc['text']))
        for target in re.findall(r'!?\[\[([^\]]+)\]\]', navigable):
            target = target.split('|')[0].split('#')[0]
            if not target:
                continue
            matches = targets.get(target, set())
            if not matches:
                errors.append(f'{path}: missing link/embed {target}')
            elif len(matches) > 1:
                errors.append(f'{path}: ambiguous link/embed {target}')
    manifests = sorted((root / '_Data').glob('visual-media-*.json'))
    verified = 0
    recorded = set()
    for manifest in manifests:
        try:
            assets = json.loads(manifest.read_text(encoding='utf-8'))['assets']
            for asset in assets:
                path = (root / asset['path']).resolve()
                if not path.is_relative_to(root.resolve()):
                    errors.append(f'{manifest.name}: media path escapes vault')
                    continue
                if path in recorded:
                    errors.append(f'{asset["path"]}: duplicate media record')
                recorded.add(path)
                if not path.is_file():
                    errors.append(f'{asset["path"]}: media missing')
                    continue
                data = path.read_bytes()
                if len(data) != asset['bytes'] or hashlib.sha256(data).hexdigest() != asset['sha256']:
                    errors.append(f'{asset["path"]}: media integrity mismatch')
                else:
                    verified += 1
        except (ValueError, KeyError, TypeError) as error:
            errors.append(f'{manifest.name}: invalid manifest: {error}')
    for path in (root / '_Media' / 'Roblox').rglob('*'):
        if path.is_file() and path.resolve() not in recorded:
            errors.append(f'{path.relative_to(root).as_posix()}: media has no integrity record')
    return {'notes': len(docs), 'media_verified': verified, 'errors': errors}


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    query = commands.add_parser('search', help='Rank local notes and show their evidence status')
    query.add_argument('query')
    query.add_argument('-k', type=int, default=3)
    query.add_argument('--json', action='store_true')
    read = commands.add_parser('read', help='Read one exact note or heading')
    read.add_argument('title')
    read.add_argument('--heading')
    commands.add_parser('check', help='Check note metadata, wikilinks, embeds and media integrity')
    args = parser.parse_args()
    if args.command == 'search':
        if not 1 <= args.k <= 50:
            parser.error('-k must be between 1 and 50')
        hits = search(ROOT, args.query, args.k)
        if args.json:
            print(json.dumps(hits, indent=2, ensure_ascii=False))
        else:
            for hit in hits:
                print(f"{hit['title']} [status: {hit['status']}]\n{hit['path']}\n{hit['summary']}\nHeadings: {' | '.join(hit['headings'])}\n")
            if not hits:
                print('No matching notes.')
    elif args.command == 'read':
        try:
            print(read_section(ROOT, args.title, args.heading))
        except ValueError as error:
            parser.error(str(error))
    else:
        result = check(ROOT)
        print(json.dumps(result, indent=2))
        return int(bool(result['errors']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
