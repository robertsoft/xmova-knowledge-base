#!/usr/bin/env python3
"""Analisa amostras .xmv procurando padrões heurísticos simples.

Gera `docs/collected/xmova_apps/samples/analysis.json` e `report.md`.
"""
import re
import json
from pathlib import Path

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
OUTJSON = SAMPLEDIR / 'analysis.json'
OUTMD = SAMPLEDIR / 'report.md'

KEYWORDS = ['pipeline', 'task', 'job', 'artifact', 'inputs', 'outputs', 'run', 'command', 'resource', 'secret', 'trigger']

def analyze_file(p: Path):
    text = p.read_text(errors='ignore')
    lines = text.splitlines()
    found = {k: [] for k in KEYWORDS}
    # find keyword occurrences with context
    for i,l in enumerate(lines):
        low = l.lower()
        for k in KEYWORDS:
            if k in low:
                context = '\n'.join(lines[max(0,i-2):i+3])
                found[k].append({'line': i+1, 'snippet': l.strip(), 'context': context.strip()[:400]})
    # simple block extraction: lines with '{' '}' or indentation-based
    blocks = []
    current = []
    for l in lines:
        if l.strip().endswith('{'):
            if current:
                blocks.append('\n'.join(current))
            current = [l]
        elif current:
            current.append(l)
            if l.strip().endswith('}'):
                blocks.append('\n'.join(current))
                current = []
    if current:
        blocks.append('\n'.join(current))

    return {'path': str(p), 'keywords': {k: len(found[k]) for k in KEYWORDS}, 'samples': found, 'blocks_count': len(blocks)}

def main():
    results = []
    for p in sorted(SAMPLEDIR.iterdir()):
        if p.is_file() and p.suffix.lower()=='.xmv':
            results.append(analyze_file(p))
    OUTJSON.write_text(json.dumps(results, indent=2))

    # gerar relatório simples
    md = ['# Análise de amostras .xmv\n']
    total = len(results)
    md.append(f'Total samples analyzed: {total}\n')
    for r in results:
        md.append(f'## {Path(r["path"]).name}\n')
        md.append(f'- Blocks detected: {r["blocks_count"]}\n')
        md.append('- Keyword counts:\n')
        for k,c in r['keywords'].items():
            if c>0:
                md.append(f'  - {k}: {c}\n')
        # include first snippets for pipeline/task if present
        for key in ('pipeline','task'):
            snippets = r['samples'].get(key, [])
            if snippets:
                md.append(f'### Exemplos de "{key}"\n')
                for s in snippets[:2]:
                    md.append(f'- L{ s["line"] }: {s["snippet"]}\n')
    OUTMD.write_text('\n'.join(md))
    print(f'Analysis written to {OUTJSON} and {OUTMD}')

if __name__ == '__main__':
    main()
