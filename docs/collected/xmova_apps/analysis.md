# Análise resumida — xMova Apps (branches `main`)

Resumo do que foi coletado e analisado das branches `main` nos projetos em `C:/dev/projects/xMova Apps`:

- Repositórios processados: 64 (pastas em `C:/dev/projects/xMova Apps`).
- Estrutura comum: presença recorrente de `src`, `.gitignore`, e `xmova-compiler-project.properties`.
- Arquivos de domínio: extensa presença de arquivos com extensão `.xmv` dentro de `src` (2.283 ocorrências), indicando uma DSL/artefato proprietária usada pela plataforma xmova.
- Outros itens frequentes: `.vscode`, `build` (scripts/artefatos de build), `docs` e `scripts` em alguns repositórios.

Inferências iniciais:

- A plataforma xmova usa uma linguagem/DSL `.xmv` cuja compilação/transformação é tratada por um compilador interno (provavelmente referenciado por `xmova-compiler-project.properties`).
- A maioria dos repositórios parece ser código-fonte de pipelines, transformações ou módulos escritos nessa DSL, não em linguagens convencionais (JS/Python/Java/Rust), o que explica a detecção "unknown" anterior.

Resultados e localização dos dados coletados

- Sumários por repositório: `docs/collected/xmova_apps/<repo>/summary.txt` (inclui detecção de linguagem).
- Top-level de cada repositório: `docs/collected/xmova_apps/<repo>/top-level.txt`.
- READMEs (quando presentes na branch `main`): `docs/collected/xmova_apps/<repo>/README.md`.

Principais oportunidades / próximos passos recomendados

1. Extrair um subconjunto representativo de arquivos `.xmv` e criar um analisador/AST para entender a gramática e padrões comuns.
2. Catalogar padrões de `Task`/`Job`/`Pipeline` (manifestos já definidos no knowledge-base) mapeando exemplos reais `.xmv` para o manifesto (`docs/schema/manifest-schema.yaml`).
3. Desenvolver um `xmova-sdk` (ou melhorar o existente) com utilitários para gerar/validar manifests a partir de `src/*.xmv`.
4. Consolidar snippets e templates em `examples/` para acelerar onboarding (ex.: conversão de `.xmv` → manifest).
5. Criar documentação interna que mapeie as convenções de projeto (naming, layout `src`, hooks, secrets) e políticas de deploy/ambientes (homolog/prod) observadas nos repositórios.

Próxima ação que posso executar agora (escolha):

- [ ] Gerar AST/parsers iniciais para `.xmv` (tentar inferir gramática a partir de amostras). 
- [ ] Agrupar exemplos padrões de `Pipeline` detectados e mapear para o manifesto criado.
- [ ] Gerar um relatório mais detalhado com exemplos por repositório (3-5 por categoria).

Arquivos gerados por esta coleta: veja `docs/collected/xmova_apps/`.
