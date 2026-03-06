#!/usr/bin/env python3
"""Mapeia blocos extraídos (`blocks_regex.json`) para manifests YAML heurísticos.

Gera arquivos em `docs/collected/xmova_apps/samples/mapped_manifests/` e um resumo
`docs/collected/xmova_apps/samples/mapped_manifests_report.md`.
"""
from pathlib import Path
import json
import re
import yaml

SAMPLEDIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
BLOCKS_FILE = SAMPLEDIR / 'blocks_regex.json'
OUT_DIR = SAMPLEDIR / 'mapped_manifests'
OUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT = SAMPLEDIR / 'mapped_manifests_report.md'


def parse_block_lines(lines):
    data = {}
    # search for recordList getRecords=NAME or getRecords=VAR
    for ln in lines:
        m = re.search(r'recordList\s+getRecords\s*[=:]?\s*([A-Za-z0-9_\-\$]+)', ln, re.I)
        if m:
            data.setdefault('recordlists', []).append(m.group(1))
        m2 = re.search(r'recordDetail\s+fields\s*[=:]?\s*([A-Za-z0-9_,]+)', ln, re.I)
        if m2:
            fields = [f.strip() for f in m2.group(1).split(',') if f.strip()]
            data.setdefault('recorddetails', []).append({'fields': fields})

        # capture simple SQL assignments: _name = Select * FROM Table (map as query resource)
        m3 = re.search(r'([A-Za-z0-9_\$]+)\s*=\s*(Select\s+\*\s+FROM\s+.+)', ln, re.I)
        if m3:
            name = m3.group(1)
            sql = m3.group(2).strip()
            data.setdefault('queries', {})[name] = sql

        # capture event/state assignments (beforeInit/beforeClose lines)
        m4 = re.search(r'^\s*([A-Za-z0-9_\$]+)\s*=\s*(null|.+)$', ln)
        if m4 and 'Select' not in ln:
            data.setdefault('assignments', []).append({m4.group(1): m4.group(2).strip()})

        # capture labels or 'labels' markers
        if re.search(r'\blabels\b', ln, re.I):
            data.setdefault('labels', []).append(ln.strip())

        # capture getRecords with possible param or resource name
        m5 = re.search(r'recordList\s+getRecords\s*[=:]?\s*([A-Za-z0-9_\-\$]+)', ln, re.I)
        if m5:
            data.setdefault('getRecords', []).append(m5.group(1))

    return data


def map_file_blocks(blocks):
    manifest = {
        'apiVersion': 'xmova/v1',
        'kind': 'Pipeline',
        'metadata': {
            'name': None
        },
        'pipeline': {
            'tasks': []
        },
        'hooks': {},
        'resources': [],
        'secrets': {}
    }
    # accumulate resources from queries
    resource_map = {}
    for b in blocks:
        btype = b.get('type')
        parsed = parse_block_lines(b.get('lines', []))

        # map queries to resources
        for qn, sql in parsed.get('queries', {}).items():
            rname = qn if qn else f'resource_{len(resource_map)+1}'
            resource_map[rname] = {'name': rname, 'type': 'sql', 'sql': sql}

    # add resources to manifest
    for r in resource_map.values():
        manifest['resources'].append(r)

    # build tasks & hooks from blocks
    for b in blocks:
        btype = b.get('type')
        parsed = parse_block_lines(b.get('lines', []))

        # recordlist/getRecords -> create task referencing resource if available
        for gr in parsed.get('getRecords', []):
            if gr in resource_map:
                task = {'id': f'get_{gr}', 'name': f'get_{gr}', 'run': {'type': 'resource_query', 'resource': gr}}
            else:
                task = {'id': f'get_{gr}', 'name': f'get_{gr}', 'run': {'type': 'query', 'source': gr}}
            manifest['pipeline']['tasks'].append(task)

        # queries also as standalone tasks
        for qn, sql in parsed.get('queries', {}).items():
            task = {'id': f'query_{qn}', 'name': f'query_{qn}', 'run': {'type': 'sql', 'sql': sql}}
            manifest['pipeline']['tasks'].append(task)

        # recorddetails -> add a transform/emit task listing fields
        for rd in parsed.get('recorddetails', []):
            fields = rd.get('fields', [])
            task = {
                'id': f'recorddetail_fields_{len(manifest["pipeline"]["tasks"]) + 1}',
                'name': 'recorddetail_fields',
                'run': {'type': 'emit'},
                'outputs': [{'name': f} for f in fields]
            }
            manifest['pipeline']['tasks'].append(task)

        # assignments -> map to hooks (detect beforeInit/beforeClose by presence in block lines)
        if parsed.get('assignments'):
            for a in parsed.get('assignments'):
                for k, v in a.items():
                    # try to place in appropriate hook
                    manifest['hooks'].setdefault('beforeInit', []).append({k: v})

        # labels -> metadata.labels (best-effort parse)
        if parsed.get('labels'):
            for lbl in parsed.get('labels'):
                # try to extract key-like label e.g. 'labels' or 'labels=...' (fall back to raw)
                manifest['metadata'].setdefault('labels', []).append(lbl)

    return manifest

    return manifest


def main():
    if not BLOCKS_FILE.exists():
        print('blocks file not found:', BLOCKS_FILE)
        return
    blocks = json.loads(BLOCKS_FILE.read_text())
    byfile = {}
    for b in blocks:
        fn = b.get('file')
        byfile.setdefault(fn, []).append(b)

    report_lines = ['# Mapped Manifests Report', '']
    for fn, blks in byfile.items():
        manifest = map_file_blocks(blks)
        manifest['metadata']['name'] = fn.replace('.xmv','')
        outp = OUT_DIR / (fn + '.yaml')
        outp.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True))
        report_lines.append(f'- {fn} -> {outp.name} (tasks: {len(manifest["pipeline"]["tasks"])})')

    REPORT.write_text('\n'.join(report_lines))
    print('Wrote manifests to', OUT_DIR)


if __name__ == '__main__':
    main()
