# Xmova Knowledge Base

> Base de Conhecimento Central para a tecnologia proprietária **xmova** — projetada para ser consumida por agentes de IA, assistentes de código e ferramentas de desenvolvimento.

## O que é este repositório?

Este repositório funciona como a **memória persistente e especializada** sobre a tecnologia xmova. Ele é continuamente enriquecido pelas interações com ferramentas de IA (GitHub Copilot, Cursor, agentes MCP etc.) e serve como fonte de verdade para qualquer assistente que trabalhe com xmova.

## Estrutura do Repositório

```
xmova-knowledge-base/
├── .github/
│   ├── agents/
│   │   └── xmova-expert.md          # Contexto e diretivas para agentes de IA
│   └── copilot-instructions.md      # Instruções customizadas para GitHub Copilot
├── .vscode/
│   └── settings.json                # Configurações recomendadas para VS Code
├── docs/
│   ├── api-reference/
│   │   └── core-concepts.md         # Conceitos centrais e API da xmova
│   ├── best-practices/
│   │   ├── naming-conventions.md    # Convenções de nomenclatura
│   │   └── coding-standards.md     # Padrões de codificação
│   └── architecture/
│       └── overview.md              # Visão geral da arquitetura xmova
├── examples/
│   └── starter-templates/
│       └── basic-project.md         # Template inicial de projeto xmova
├── .cursorrules                     # Regras para Cursor IDE e editores compatíveis
├── CONTRIBUTING.md                  # Guia para contribuir e evoluir a base de conhecimento
└── README.md                        # Este arquivo
```

## Como usar com Ferramentas de IA

### GitHub Copilot (VS Code / GitHub.com)

O Copilot lê automaticamente o arquivo `.github/copilot-instructions.md` para aplicar instruções customizadas ao repositório. Os arquivos em `.github/agents/` fornecem contexto aprofundado para os agentes do Copilot.

### Cursor IDE

O arquivo `.cursorrules` é carregado automaticamente pelo Cursor, aplicando as regras de desenvolvimento xmova a toda a sessão de codificação.

### MCP (Model Context Protocol)

A estrutura deste repositório é compatível com servidores de arquivos MCP. Aponte seu servidor MCP para a raiz deste repositório e os agentes terão acesso ao conhecimento completo sobre xmova.

### VS Code + Qualquer LLM

1. Clone este repositório localmente.
2. Abra-o no VS Code com as configurações em `.vscode/settings.json`.
3. Use o indexador de codebase do seu plugin de IA preferido apontando para este diretório.

## Como Clonar e Usar Localmente

```bash
git clone https://github.com/robertsoft/xmova-knowledge-base.git
cd xmova-knowledge-base
```

Após clonar, abra o diretório no seu editor de código favorito. As configurações e regras serão aplicadas automaticamente.

## Como Evoluir este Repositório

Toda vez que uma nova descoberta, padrão, solução ou conceito sobre xmova for identificado, ele deve ser documentado aqui. Consulte o [CONTRIBUTING.md](./CONTRIBUTING.md) para o processo detalhado.

## Licença

Este repositório contém conhecimento proprietário sobre a tecnologia xmova e é de uso interno.
