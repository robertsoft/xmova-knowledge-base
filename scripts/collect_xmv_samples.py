#!/usr/bin/env python3
"""Coleta amostras .xmv de repositórios em C:/dev/projects/xMova Apps

Uso: python scripts/collect_xmv_samples.py [max_samples]
"""
import sys
import os
import shutil
from pathlib import Path

BASE = Path(r'C:/dev/projects/xMova Apps')
OUTDIR = Path(r'c:/xmova-knowledge-base/docs/collected/xmova_apps/samples')

def main():
    max_samples = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    OUTDIR.mkdir(parents=True, exist_ok=True)
    collected = 0
    for repo in sorted(BASE.iterdir()):
        if collected >= max_samples:
            break
        src_dir = repo / 'src'
        if not src_dir.is_dir():
            continue
        # procurar por arquivos .xmv
        for root,_,files in os.walk(src_dir):
            for f in files:
                if f.lower().endswith('.xmv'):
                    rel = Path(root).relative_to(BASE)
                    dest_name = f"{repo.name}--{rel.as_posix().replace('/','_')}--{f}"
                    dest = OUTDIR / dest_name
                    try:
                        shutil.copyfile(Path(root)/f, dest)
                        collected += 1
                    except Exception:
                        continue
                    if collected >= max_samples:
                        break
            if collected >= max_samples:
                break

    print(f"Collected {collected} samples into {OUTDIR}")

if __name__ == '__main__':
    main()
