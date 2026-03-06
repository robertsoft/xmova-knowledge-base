#!/usr/bin/env python3
"""Runner simples para manifests xmova.

Este runner executa as `command` de cada `Task` localmente via shell, na ordem definida.
Não usa containers — é uma ferramenta de demonstração para desenvolvimento.
"""
import sys
import yaml
from pathlib import Path
import subprocess

def run_task(task):
    print(f"==> Executando task: {task.get('id')}")
    run = task.get('run', {})
    cmd = run.get('command')
    if not cmd:
        print("Nenhum comando definido para task; pulando.")
        return 0
    # Se command for array, execute como lista; se string, execute via shell
    try:
        if isinstance(cmd, list):
            res = subprocess.run(cmd, check=False)
        else:
            res = subprocess.run(cmd, shell=True, check=False)
        print(f"Task {task.get('id')} exit: {res.returncode}")
        return res.returncode
    except Exception as e:
        print(f"Erro executando task: {e}")
        return 4

def main():
    if len(sys.argv) != 2:
        print("Usage: run-manifest.py <manifest.yaml>")
        sys.exit(2)
    manifest_path = Path(sys.argv[1])
    if not manifest_path.exists():
        print("Manifesto não encontrado.")
        sys.exit(2)

    m = yaml.safe_load(manifest_path.read_text())
    tasks = m.get('pipeline', {}).get('tasks', [])
    for task in tasks:
        code = run_task(task)
        if code != 0:
            print("Pipeline abortado devido a falha na task.")
            sys.exit(code)

    # executar hooks post se existirem
    hooks = m.get('hooks', {})
    for cmd in hooks.get('post', []):
        print(f"Executando hook post: {cmd}")
        subprocess.run(cmd, shell=True)

    print("Pipeline concluído com sucesso.")

if __name__ == '__main__':
    main()
