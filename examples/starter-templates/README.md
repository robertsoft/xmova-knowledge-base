# Exemplo de Manifesto xmova

Este diretório contém um manifesto de exemplo (`manifest-example.yaml`) e um pequeno runner para executar o pipeline localmente.

Requisitos:

- Python 3
- (opcional) `docker` se preferir executar cada `Task` em containers

Executar validação do manifesto:

```bash
python scripts/validate_manifest.py examples/starter-templates/manifest-example.yaml
```

Executar o runner local (simula execução das tasks no host):

```bash
python examples/starter-templates/run-manifest.py examples/starter-templates/manifest-example.yaml
```
