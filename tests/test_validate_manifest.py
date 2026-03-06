import subprocess
import sys
from pathlib import Path


def test_validate_example_manifest():
    py = sys.executable
    manifest = Path('examples/starter-templates/manifest-example.yaml')
    assert manifest.exists()
    res = subprocess.run([py, 'scripts/validate_manifest.py', str(manifest)])
    assert res.returncode == 0
