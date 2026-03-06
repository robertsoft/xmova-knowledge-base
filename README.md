# Xmova Knowledge Base
Este repositório serve como a **Base de Conhecimento Central** para a tecnologia proprietária **xmova**.

## Como usar com IAs:
- **GitHub Copilot:** O agente lerá automaticamente os arquivos em `.github/agents/`.
- **Cursor/VS Code:** Utilize o indexador de codebase apontando para este repositório.
- **MCP:** Esta estrutura é compatível com servidores de arquivos para o Model Context Protocol.

## Setup rápido (desenvolvimento)

Instale dependências úteis para validação/execução dos exemplos:

```bash
pip install -r requirements.txt
```

Validar o manifesto de exemplo:

```bash
python scripts/validate_manifest.py examples/starter-templates/manifest-example.yaml
```

Executar o runner de demonstração (simula execução local das `Task`s):

```bash
python examples/starter-templates/run-manifest.py examples/starter-templates/manifest-example.yaml
```

Os arquivos de referência:
- Schema do manifesto: [docs/schema/manifest-schema.json](docs/schema/manifest-schema.json#L1)
- Documento do manifesto: [docs/api-reference/manifest.md](docs/api-reference/manifest.md#L1)
- Exemplo: [examples/starter-templates/manifest-example.yaml](examples/starter-templates/manifest-example.yaml#L1)

