import subprocess
import sys
from pathlib import Path


def test_run_example_manifest():
    py = sys.executable
    manifest = Path('examples/starter-templates/manifest-example.yaml')
    assert manifest.exists()
    res = subprocess.run([py, 'examples/starter-templates/run-manifest.py', str(manifest)])
    assert res.returncode == 0
