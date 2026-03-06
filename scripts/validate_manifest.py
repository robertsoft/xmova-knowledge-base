#!/usr/bin/env python3
"""Valida um manifesto xmova usando JSON Schema.

Uso: python scripts/validate_manifest.py <manifest.yaml>
"""
import sys
import json
import yaml
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("Dependência 'jsonschema' não encontrada. Instale com: pip install jsonschema pyyaml")
    sys.exit(2)

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_manifest.py <manifest.yaml>")
        sys.exit(2)
    manifest_path = Path(sys.argv[1])
    if not manifest_path.exists():
        print(f"Arquivo não encontrado: {manifest_path}")
        sys.exit(2)

    schema_path = Path(__file__).parents[1] / 'docs' / 'schema' / 'manifest-schema.json'
    if not schema_path.exists():
        print(f"Schema não encontrado: {schema_path}")
        sys.exit(2)

    manifest = yaml.safe_load(manifest_path.read_text())
    schema = json.loads(schema_path.read_text())

    try:
        jsonschema.validate(instance=manifest, schema=schema)
        print("Manifesto válido.")
        return 0
    except jsonschema.exceptions.ValidationError as e:
        print("Validação falhou:")
        print(e.message)
        return 3

if __name__ == '__main__':
    sys.exit(main())
