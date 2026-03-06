#!/usr/bin/env python3
"""Converter BNF gerada em gramática Lark e testar linhas das amostras.
"""
from lark import Lark
from pathlib import Path

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
BNF = SAMPLEDIR / 'generated_grammar.bnf'

def bnf_to_lark(bnf_text):
    lines = [l.strip() for l in bnf_text.splitlines() if l.strip()]
    rules = []
    names = []
    for l in lines:
        if '::=' in l:
            left,right = l.split('::=',1)
            name = left.strip().strip('<>').strip()
            names.append(name)
            # sanitize right side: replace placeholder tokens with terminals
            rhs_parts = []
            for part in right.strip().split():
                p = part.strip()
                if '<STR>' in p or '"<STR>"' in p or p=='<STR>':
                    rhs_parts.append('STRING')
                elif '<NUM>' in p or p=='<NUM>':
                    rhs_parts.append('NUMBER')
                elif '<PATH>' in p or p=='/<PATH>':
                    rhs_parts.append('PATH')
                else:
                    # ensure quoted literals are valid Lark strings
                    if p.startswith('"') and p.endswith('"'):
                        lit = p[1:-1].replace('"','\\"')
                        rhs_parts.append(f'"{lit}"')
                    else:
                        rhs_parts.append(p)
            rules.append(f"{name}: {' '.join(rhs_parts)}")
    # define common imports and terminals (PATH is custom)
    header = (
        "%import common.WS\n"
        "%import common.NUMBER\n"
        "%import common.ESCAPED_STRING -> STRING\n"
        "%ignore WS\n\n"
    )
    # custom terminal for file/path-like tokens
    header += "PATH: /[A-Za-z0-9_.\\/\\-]+/\n\n"
    start = "start: (" + " | ".join(names) + ")+\n\n"
    return header + start + "\n".join(rules)

def test_parser(grammar):
    parser = Lark(grammar, parser='lalr')
    total=0
    matched=0
    for p in sorted(SAMPLEDIR.glob('*.xmv'))[:3]:
        for l in p.read_text(errors='ignore').splitlines():
            s=l.strip()
            if not s:
                continue
            total+=1
            try:
                parser.parse(s)
                matched+=1
            except Exception:
                pass
    return matched, total

def main():
    if not BNF.exists():
        print('BNF not found:', BNF)
        return
    g = bnf_to_lark(BNF.read_text())
    m,t = test_parser(g)
    pct = (m/t*100) if t else 0
    print(f'BNF-Lark matched {m}/{t} lines ({pct:.1f}%)')

if __name__=='__main__':
    main()
