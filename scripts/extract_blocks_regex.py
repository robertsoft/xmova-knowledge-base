#!/usr/bin/env python3
"""Extrator simples por regex para blocos `recorddetail`, `recordlist`, `views` nas amostras .xmv

Gera `blocks_regex.json` e `blocks_regex_report.md` em `docs/collected/xmova_apps/samples`.
"""
import re
import json
from pathlib import Path

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
OUT_JSON = SAMPLEDIR / 'blocks_regex.json'
OUT_MD = SAMPLEDIR / 'blocks_regex_report.md'

BLOCK_START_RE = re.compile(r'^(recorddetail|recordlist|views?)\b', re.I)
TOP_LEVEL_RE = re.compile(r'^[a-z0-9_\.]+\b', re.I)
# key/value inside blocks
KV_RE = re.compile(r'^\s*([A-Za-z0-9_\.]+)\s*(?:=|:)\s*(.+)$')


def extract_blocks(path: Path):
    text = path.read_text(errors='ignore').splitlines()
    blocks = []
    i = 0
    while i < len(text):
        line = text[i]
        m = BLOCK_START_RE.match(line.strip())
        if m:
            btype = m.group(1).lower()
            start = i + 1
            collected = [line.rstrip()]
            i += 1
            # collect until blank line or next top-level token
            while i < len(text):
                nxt = text[i]
                if not nxt.strip():
                    break
                if TOP_LEVEL_RE.match(nxt) and not nxt.startswith(' '):
                    # consider this a new top-level entry
                    break
                collected.append(nxt.rstrip())
                i += 1
            end = i
            # parse inner key/values inside the block
            kvs = []
            for ln in collected[1:]:
                m2 = KV_RE.match(ln)
                if m2:
                    key = m2.group(1).strip()
                    val = m2.group(2).strip()
                    # remove surrounding quotes if present
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    kvs.append({'key': key, 'value': val, 'raw': ln.strip()})

            blocks.append({
                'file': str(path.name),
                'type': btype,
                'start_line': start,
                'end_line': end,
                'lines': collected,
                'kv': kvs,
            })
        else:
            i += 1
    return blocks


def main():
    samples = sorted([x for x in SAMPLEDIR.iterdir() if x.suffix.lower()=='.xmv'])
    all_blocks = []
    counts = {}
    for s in samples:
        bs = extract_blocks(s)
        all_blocks.extend(bs)
        for b in bs:
            counts[b['type']] = counts.get(b['type'], 0) + 1

    OUT_JSON.write_text(json.dumps(all_blocks, indent=2, ensure_ascii=False))

    lines = [
        '# Regex Blocks Report',
        f'Total samples scanned: {len(samples)}',
        '',
        '## Block counts',
    ]
    for k,v in sorted(counts.items(), key=lambda kv: -kv[1]):
        lines.append(f'- **{k}**: {v}')

    lines.append('')
    lines.append('## Example block (first)')
    if all_blocks:
        ex = all_blocks[0]
        lines.append(f"- file: {ex['file']}")
        lines.append(f"- type: {ex['type']}")
        lines.append('')
        lines.append('```')
        lines.extend(ex['lines'][:200])
        lines.append('```')

    OUT_MD.write_text('\n'.join(lines))
    print('Wrote', OUT_JSON, 'and', OUT_MD)


if __name__ == '__main__':
    main()
