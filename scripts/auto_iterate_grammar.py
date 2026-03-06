#!/usr/bin/env python3
"""Itera automaticamente a gramática Lark: coleta linhas não reconhecidas,
infere regras simples e reavalia cobertura até convergência ou máximo de iterações.

Gera gramáticas em `scripts/grammar_iter_<n>.lark` e grava `grammar_iteration_report.md`.
"""
from lark import Lark
from pathlib import Path
import re
import json

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
OUT_DIR = Path('c:/xmova-knowledge-base/scripts')
OUT_REPORT = OUT_DIR / 'grammar_iteration_report.md'

BASE_GRAMMAR = r'''
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
    | custom_stmt
    | path_stmt
    | assign_stmt
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
path_stmt: /\/\S+/
assign_stmt: NAME (":"|"=") (STRING|NUMBER|NAME|PATH)
generic: NAME ("." NAME)*

PATH: /\/[A-Za-z0-9_\.\/\-]+/
'''


def build_parser(grammar_text):
    return Lark(grammar_text, parser='lalr', propagate_positions=False, maybe_placeholders=False)


def test_parser_and_collect_unmatched(parser):
    total = 0
    matched = 0
    unmatched = []
    for p in sorted([x for x in SAMPLEDIR.iterdir() if x.suffix.lower()=='.xmv']):
        for l in p.read_text(errors='ignore').splitlines():
            s = l.strip()
            if not s:
                continue
            total += 1
            try:
                parser.parse(s)
                matched += 1
            except Exception:
                unmatched.append(s)
    return matched, total, unmatched


def infer_simple_rules(unmatched_lines):
    # heurísticas simples que geram regras Lark se padrões detectados
    rules = {}
    # key = rule_name, value = rule_definition (string)

    # pattern: key(:|=)"..."
    if any(re.search(r"^[-_a-zA-Z0-9\.]+\s*[:=]\s*\".*\"$", l) for l in unmatched_lines):
        rules['kv_string'] = 'kv_string: NAME (":"|"=") STRING'

    # pattern: key(:|=)number
    if any(re.search(r"^[-_a-zA-Z0-9\.]+\s*[:=]\s*\d+$", l) for l in unmatched_lines):
        rules['kv_number'] = 'kv_number: NAME (":"|"=") NUMBER'

    # dotted keys with assignment: custom.msg = "..."
    if any(re.search(r"^[-_a-zA-Z0-9\.]+\s*[:=]\s*\".*\"$", l) for l in unmatched_lines):
        rules['dotted_assign'] = 'dotted_assign: (NAME "." NAME)+ (":"|"=") STRING'

    # unquoted assignment to names
    if any(re.search(r"^[-_a-zA-Z0-9\.]+\s*[:=]\s*[-_a-zA-Z0-9\.]+$", l) for l in unmatched_lines):
        rules['kv_name'] = 'kv_name: NAME (":"|"=") NAME'

    # lines starting with lower-case words followed by space (commands)
    if any(re.search(r"^[a-z][a-z0-9_]+\s+", l) for l in unmatched_lines):
        rules['command_like'] = 'command_like: NAME (NAME|STRING|NUMBER)*'

    return rules


def main():
    grammar = BASE_GRAMMAR
    report_lines = ['# Grammar iteration report', '']
    prev_matched = -1
    max_iters = 6
    for it in range(1, max_iters+1):
        try:
            parser = build_parser(grammar)
        except Exception as e:
            report_lines.append(f'Iteration {it}: failed to build parser: {e}')
            break

        matched, total, unmatched = test_parser_and_collect_unmatched(parser)
        pct = (matched/total*100) if total else 0
        report_lines.append(f'Iteration {it}: matched {matched}/{total} ({pct:.1f}%)')
        # save current grammar
        gfile = OUT_DIR / f'grammar_iter_{it}.lark'
        gfile.write_text(grammar)

        # stop if no improvement
        if matched <= prev_matched and prev_matched != -1:
            report_lines.append('No improvement; stopping')
            break

        prev_matched = matched

        # infer rules from unmatched
        new_rules = infer_simple_rules(unmatched)
        if not new_rules:
            report_lines.append('No new rules inferred; stopping')
            break

        # append new rules to grammar if not already present
        added = 0
        for name, rule in new_rules.items():
            if rule not in grammar:
                grammar += '\n' + rule + '\n'
                added += 1

        report_lines.append(f'Inferred {len(new_rules)} candidate rules, added {added}')

    # save unmatched sample lines for inspection
    try:
        parser = build_parser(grammar)
        matched, total, unmatched = test_parser_and_collect_unmatched(parser)
        (OUT_DIR / 'unmatched_lines.json').write_text(json.dumps(unmatched[:500], ensure_ascii=False, indent=2))
    except Exception:
        pass

    OUT_REPORT.write_text('\n'.join(report_lines))
    print('Iteration finished; report at', OUT_REPORT)


if __name__ == '__main__':
    main()
