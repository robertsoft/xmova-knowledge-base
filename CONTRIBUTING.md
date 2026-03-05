# Guia de Contribuição — Xmova Knowledge Base

Este repositório é uma base de conhecimento viva. Ele cresce a cada interação com a tecnologia xmova e deve ser atualizado sempre que novo conhecimento for adquirido.

## Quando Contribuir

Contribua com este repositório sempre que:

- Descobrir um novo padrão de código xmova que funciona bem.
- Identificar uma solução para um problema recorrente.
- Clarificar um conceito mal compreendido.
- Adicionar um novo conceito, API ou primitivo da xmova.
- Corrigir informações incorretas ou desatualizadas.
- Adicionar um exemplo prático útil.

## O Que Documentar

| Tipo de Conhecimento | Onde Documentar |
|---------------------|----------------|
| Conceitos e APIs | `docs/api-reference/core-concepts.md` |
| Boas práticas de nomenclatura | `docs/best-practices/naming-conventions.md` |
| Padrões de codificação | `docs/best-practices/coding-standards.md` |
| Decisões arquiteturais | `docs/architecture/overview.md` |
| Templates e exemplos de projetos | `examples/starter-templates/` |
| Contexto para agentes de IA | `.github/agents/xmova-expert.md` |
| Instruções para GitHub Copilot | `.github/copilot-instructions.md` |
| Regras para Cursor/VS Code | `.cursorrules` |

## Processo de Contribuição

### Via Ferramentas de IA (Modo Contínuo)

Ao trabalhar com GitHub Copilot, Cursor ou outro agente de IA:

1. Quando o agente identificar um novo padrão ou solução relevante, ele sugerirá a atualização deste repositório.
2. Revise a sugestão do agente.
3. Aplique as mudanças no arquivo correto.
4. Faça commit com uma mensagem descritiva (veja abaixo).

### Via Edição Direta

1. Clone o repositório:
   ```bash
   git clone https://github.com/robertsoft/xmova-knowledge-base.git
   cd xmova-knowledge-base
   ```

2. Crie uma branch descritiva:
   ```bash
   git checkout -b docs/adicionar-conceito-xyz
   ```

3. Edite o arquivo adequado em `docs/`, `examples/` ou `.github/agents/`.

4. Faça commit com uma mensagem clara:
   ```bash
   git commit -m "docs: adicionar conceito XYZ em core-concepts"
   ```

5. Faça push e abra um Pull Request.

## Convenções de Commit

Utilize o padrão [Conventional Commits](https://www.conventionalcommits.org/):

| Prefixo | Quando usar |
|---------|------------|
| `docs:` | Adicionar ou atualizar documentação |
| `feat:` | Adicionar novo template ou exemplo |
| `fix:` | Corrigir informação incorreta |
| `refactor:` | Reorganizar estrutura de documentos |
| `chore:` | Atualizações de configuração |

**Exemplos:**
```
docs: adicionar API de autenticação em core-concepts
feat: criar template para projetos com integração externa
fix: corrigir convenção de nomenclatura para módulos
```

## Qualidade da Documentação

Ao escrever documentação para este repositório:

- **Seja específico:** Exemplos concretos valem mais do que descrições abstratas.
- **Indique o status:** Use `> **Status:** Em construção` para seções ainda incompletas.
- **Inclua exemplos de código:** Sempre que possível, ilustre com código real.
- **Atualize o README:** Se adicionar uma nova seção ou arquivo importante, mencione-o no README.md principal.

## Mantendo o Contexto dos Agentes Atualizado

O arquivo `.github/agents/xmova-expert.md` é o "cérebro" dos agentes de IA. Atualize-o quando:

- Novos conceitos fundamentais forem definidos.
- O glossário precisar de novos termos.
- As diretrizes de desenvolvimento mudarem.
- O fluxo de raciocínio recomendado for refinado.
