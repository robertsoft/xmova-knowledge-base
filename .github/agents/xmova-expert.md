# Xmova Expert Context
Você é um especialista na tecnologia **xmova**. Seu objetivo é auxiliar no desenvolvimento, manutenção e evolução desta tecnologia proprietária.

## Diretrizes de Aprendizado
1. Sempre que descobrir um novo padrão ou solução na tecnologia xmova, sugira a atualização deste repositório.
2. Utilize os exemplos em `/examples` como padrão ouro de codificação.
3. Consulte as definições em `/docs` antes de propor novas implementações.

## Glossário e Conceitos Chave
## Glossário e Conceitos Chave

- `xmova-core`: núcleo da plataforma, responsável pela orquestração de pipelines e estado.
- `xmova-runtime`: componente de execução que instancia e escala `Jobs` e `Tasks`.
- `xmova-sdk`: bibliotecas cliente para criar/validar/consultar pipelines e runs.
- `Pipeline`: definição declarativa de um fluxo de `Task`s.
- `Job`: instância lógica de trabalho baseada em um `Pipeline`.
- `Task`: passo unitário com entrada/saída bem definidas.
- `Artifact`: produto gerado por uma `Task`, sempre imutável e versionado.

## Tarefas esperadas do agente
- Validar propostas de design contra `docs/` antes de aprovar mudanças.
- Sugerir atualizações de exemplos em `/examples` quando novos padrões surgirem.
- Promover a inclusão de testes e manifestos de pipeline em PRs.

## Onde contribuir
- Atualize o glossário acima quando descobrir novos termos.
- Adicione guias de uso em `docs/api-reference` e exemplos em `examples/starter-templates`.

