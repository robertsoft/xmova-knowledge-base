#!/usr/bin/env python3
"""Valida todos os manifests YAML gerados contra o JSON Schema e gera um relatório.

Gera `docs/collected/xmova_apps/samples/manifest_validation_report.md`.
"""
from pathlib import Path
import json
import yaml
try:
    import jsonschema
except ImportError:
    print("Dependência 'jsonschema' não encontrada. Instale com: pip install jsonschema pyyaml")
    raise

SAMPLES_DIR = Path('c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')
MANIFEST_DIR = SAMPLES_DIR / 'mapped_manifests'
REPORT = SAMPLES_DIR / 'manifest_validation_report.md'
SCHEMA = Path(__file__).parents[1] / 'docs' / 'schema' / 'manifest-schema.json'


def load_schema():
    if not SCHEMA.exists():
        raise SystemExit(f'Schema não encontrado: {SCHEMA}')
    return json.loads(SCHEMA.read_text())


def validate_file(path, schema):
    try:
        data = yaml.safe_load(path.read_text())
    except Exception as e:
        return False, f'YAML parse error: {e}'
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, 'OK'
    except jsonschema.exceptions.ValidationError as e:
        return False, e.message


def main():
    schema = load_schema()
    files = sorted([p for p in MANIFEST_DIR.iterdir() if p.suffix in ('.yml', '.yaml')])
    if not files:
        print('No manifests found in', MANIFEST_DIR)
        return
    lines = ['# Manifest Validation Report', '']
    failures = 0
    for f in files:
        ok, msg = validate_file(f, schema)
        status = 'VALID' if ok else 'INVALID'
        lines.append(f'- {f.name}: {status} - {msg}')
        if not ok:
            failures += 1

    lines.append('')
    lines.append(f'Total: {len(files)}, Failures: {failures}')
    REPORT.write_text('\n'.join(lines))
    print('Wrote report to', REPORT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
