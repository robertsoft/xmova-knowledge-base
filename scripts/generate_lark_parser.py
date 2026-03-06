#!/usr/bin/env python3
"""Gerar e testar um parser Lark protótipo para a DSL .xmv

Este script tenta aplicar uma gramática heurística a linhas das amostras
e reporta quantas linhas foram reconhecidas.
"""
from lark import Lark
from pathlib import Path

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')

GRAMMAR = r'''
%import common.WS
%import common.NUMBER
%import common.CNAME -> NAME
%import common.ESCAPED_STRING -> STRING
%ignore WS

start: stmt*

?stmt: view_stmt
    | fieldlabel_stmt
    | entitylabel_stmt
    | if_stmt
    | recordlist_stmt
    | recorddetail_stmt
    | assign_stmt
    | custom_stmt
    | path_stmt
    | recorddetail_block
    | recordlist_block
    | view_block
    | generic

view_stmt: "views"
fieldlabel_stmt: "fieldlabel" NAME
entitylabel_stmt: "entitylabel" NAME
if_stmt: "if" NAME comp_op (NUMBER|NAME)
comp_op: "=="|"!="|">"|"<"|"="
recordlist_stmt: "recordlist" NAME
recorddetail_stmt: "recorddetail" NAME ("fields" "=" name_list)?
name_list: NAME ("," NAME)*
custom_stmt: "custom" ("." NAME)+ ("=" STRING)?
assign_stmt: NAME (":"|"=") (STRING|NUMBER|NAME|PATH)
path_stmt: /\/\S+/
 # message_stmt removed to avoid ambiguity with custom dotted names
message_stmt: (NAME "." NAME)+ ("=" STRING)?
generic: NAME ("." NAME)*

recorddetail_block: /(?i)recorddetail/ /.+/
recordlist_block: /(?i)recordlist/ /.+/
view_block: /(?i)views?/ /.+/

PATH: /\/[A-Za-z0-9_\.\/\-]+/
'''


def build_parser():
    return Lark(GRAMMAR, parser='lalr', propagate_positions=False, maybe_placeholders=False)


def test_on_file(parser, path: Path):
    lines = path.read_text(errors='ignore').splitlines()
    total = 0
    matched = 0
    for l in lines:
        s = l.strip()
        if not s:
            continue
        total += 1
        try:
            parser.parse(s.lower())
            matched += 1
        except Exception:
            pass
    return total, matched


def main():
    p = build_parser()
    samples = sorted([x for x in SAMPLEDIR.iterdir() if x.suffix.lower()=='.xmv'])[:3]
    if not samples:
        print('No samples found in', SAMPLEDIR)
        return
    overall_total = 0
    overall_matched = 0
    for s in samples:
        tot, mat = test_on_file(p, s)
        overall_total += tot
        overall_matched += mat
        print(f'{s.name}: {mat}/{tot} lines matched')

    pct = (overall_matched / overall_total * 100) if overall_total else 0
    print(f'Overall: {overall_matched}/{overall_total} lines matched ({pct:.1f}%)')


if __name__ == '__main__':
    main()
