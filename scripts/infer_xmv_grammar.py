#!/usr/bin/env python3
"""Inferir padrões e candidatos a gramática a partir das amostras .xmv.

Gera:
- docs/collected/xmova_apps/samples/grammar_candidates.json
- docs/collected/xmova_apps/samples/grammar_report.md

Uso: python scripts/infer_xmv_grammar.py
"""
from pathlib import Path
import re
import json
from collections import Counter

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
OUTJSON = SAMPLEDIR / 'grammar_candidates.json'
OUTMD = SAMPLEDIR / 'grammar_report.md'

def normalize_line(line: str) -> str:
    s = line.strip()
    # replace quoted strings
    s = re.sub(r'".*?"|\'.*?\'', '"<STR>"', s)
    # replace numbers
    s = re.sub(r'\b\d+[\d\.]*\b', '<NUM>', s)
    # replace paths
    s = re.sub(r'(/[\w\-\.]+)+', '<PATH>', s)
    # collapse multiple spaces
    s = re.sub(r'\s+', ' ', s)
    return s

def tokens(line: str):
    return re.findall(r"[A-Za-z0-9_]+", line)

def analyze():
    token_counts = Counter()
    start_counts = Counter()
    norm_counts = Counter()
    bigrams = Counter()
    files = []

    for p in sorted(SAMPLEDIR.glob('*.xmv')):
        files.append(p.name)
        text = p.read_text(errors='ignore')
        lines = [l for l in text.splitlines() if l.strip()]
        for l in lines:
            norm = normalize_line(l)
            norm_counts[norm] += 1
            tks = tokens(l)
            for t in tks:
                if len(t) >= 2:
                    token_counts[t.lower()] += 1
            if tks:
                start_counts[tks[0].lower()] += 1
            # bigrams
            for a,b in zip(tks, tks[1:]):
                bigrams[(a.lower(), b.lower())] += 1

    # derive candidate patterns: take top normalized lines
    top_norm = norm_counts.most_common(40)
    top_tokens = token_counts.most_common(200)
    top_starts = start_counts.most_common(50)
    top_bigrams = bigrams.most_common(50)

    candidates = {
        'files_analyzed': files,
        'top_tokens': top_tokens,
        'top_line_starts': top_starts,
        'top_normalized_lines': top_norm,
        'top_bigrams': [ [a+' '+b, c] for (a,b),c in top_bigrams ],
    }

    OUTJSON.write_text(json.dumps(candidates, indent=2))

    # write markdown report
    md = []
    md.append('# Grammar inference report for .xmv samples\n')
    md.append(f'Files analyzed: {len(files)}\n')
    md.append('## Top tokens\n')
    for t,c in top_tokens[:40]:
        md.append(f'- {t}: {c}\n')
    md.append('\n## Top line starts (likely keywords)\n')
    for t,c in top_starts[:40]:
        md.append(f'- {t}: {c}\n')
    md.append('\n## Top normalized line patterns\n')
    for l,c in top_norm[:40]:
        md.append(f'- ({c}) `{l}`\n')
    md.append('\n## Top token bigrams\n')
    for (pair,count) in top_bigrams[:40]:
        (a,b)=pair
        md.append(f'- {a} {b}: {count}\n')

    md.append('\n## Observations and next steps\n')
    md.append('- Tokens and line-starts suggest a keyword-driven DSL (many uppercase identifiers).\n')
    md.append('- Normalized line patterns provide candidate production rules (convert placeholders `<STR>`/`<NUM>` to terminals).\n')
    md.append('- Próximo: mapear padrões comuns para regras BNF e tentar parse com um parser gerado (e.g., lark).\n')

    OUTMD.write_text('\n'.join(md))

    print(f'Wrote {OUTJSON} and {OUTMD}')

if __name__ == '__main__':
    analyze()
