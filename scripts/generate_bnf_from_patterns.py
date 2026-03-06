#!/usr/bin/env python3
"""Gerar BNF simples a partir de patterns normalizados extraídos (grammar_candidates.json).

Gera `docs/collected/xmova_apps/samples/generated_grammar.bnf` e `bnf_report.md`.
"""
import json
from pathlib import Path

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
INPUT = SAMPLEDIR / 'grammar_candidates.json'
OUTBNF = SAMPLEDIR / 'generated_grammar.bnf'
OUTMD = SAMPLEDIR / 'bnf_report.md'

PLACEHOLDERS = ['<STR>','<NUM>','<PATH>']

def pattern_to_rule(norm_line, idx):
    # replace placeholders with tokens
    rule_name = f'R{idx}'
    parts = norm_line.split()
    rhs = []
    for p in parts:
        if p in PLACEHOLDERS:
            if p=='<STR>':
                rhs.append('STRING')
            elif p=='<NUM>':
                rhs.append('NUMBER')
            else:
                rhs.append('PATH')
        else:
            # sanitize symbol
            sym = p.replace("'","\'")
            rhs.append(f'"{sym}"')
    return rule_name, ' '.join(rhs)

def main():
    if not INPUT.exists():
        print('Input not found:', INPUT)
        return
    data = json.loads(INPUT.read_text())
    top = data.get('top_normalized_lines', [])
    lines = [l for l,c in top]
    rules = []
    md = ['# Generated BNF from patterns']
    for i,(l,c) in enumerate(top[:50], start=1):
        rule, rhs = pattern_to_rule(l, i)
        rules.append(f'<{rule}> ::= {rhs}')
        md.append(f'- {rule}: ({c}) `{l}`')

    OUTBNF.write_text('\n'.join(rules))
    OUTMD.write_text('\n'.join(md))
    print('Wrote', OUTBNF, 'and', OUTMD)

if __name__=='__main__':
    main()
