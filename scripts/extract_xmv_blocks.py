#!/usr/bin/env python3
"""Extrai blocos heurísticos de interesse de arquivos .xmv.

Procura por blocos que iniciam com palavras-chave: recorddetail, recordlist, views, events, fieldlabel, custom
e captura linhas seguintes até próximo bloco/top-level ou linha vazia.
Gera `docs/collected/xmova_apps/samples/blocks.json` e `blocks_report.md`.
"""
from pathlib import Path
import json
import re

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
OUTJSON = SAMPLEDIR / 'blocks.json'
OUTMD = SAMPLEDIR / 'blocks_report.md'

KEYWORDS = ['recorddetail','recordlist','views','events','fieldlabel','custom']

def is_start(line):
    s=line.strip()
    if not s:
        return False
    lower=s.lower()
    for k in KEYWORDS:
        if lower.startswith(k):
            return True
    return False

def extract_blocks(text):
    lines=text.splitlines()
    blocks=[]
    curr=None
    for l in lines:
        if is_start(l):
            if curr:
                blocks.append(curr)
            curr={'start_line': len(blocks)+1, 'header': l.strip(), 'lines': []}
        else:
            if curr:
                # stop block on empty line or next header
                if l.strip()=='' and curr['lines']:
                    blocks.append(curr)
                    curr=None
                else:
                    curr['lines'].append(l.rstrip())
    if curr:
        blocks.append(curr)
    return blocks

def main():
    out=[]
    for p in sorted(SAMPLEDIR.glob('*.xmv')):
        txt=p.read_text(errors='ignore')
        blocks=extract_blocks(txt)
        if blocks:
            out.append({'file': p.name, 'blocks': blocks, 'count': len(blocks)})

    OUTJSON.write_text(json.dumps(out, indent=2))

    md=['# Blocks report']
    for f in out:
        md.append(f"## {f['file']} — {f['count']} blocks")
        for b in f['blocks']:
            md.append(f"- {b['header']}")
            md.append('```')
            md.extend(b['lines'][:10])
            md.append('```')
    OUTMD.write_text('\n'.join(md))
    print(f'Wrote {OUTJSON} and {OUTMD}')

if __name__=='__main__':
    main()
