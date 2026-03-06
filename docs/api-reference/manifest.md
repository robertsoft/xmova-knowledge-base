# Manifesto de Pipeline (xmova)

Este documento descreve o formato do manifesto declarativo usado para definir pipelines no xmova.

Principais campos:

- `apiVersion`: versão do esquema (ex.: `v1`).
- `kind`: tipo de manifesto, atualmente `Pipeline`.
- `metadata`: informações como `name` e `version`.
- `pipeline.tasks`: lista ordenada de `Task`s com `id`, `run`, `inputs` e `outputs`.
- `hooks`: comandos opcionais `pre` e `post` para execução externa.

Arquivo de esquema: `docs/schema/manifest-schema.yaml`.

Exemplo prático: `examples/starter-templates/manifest-example.yaml`.

Boas práticas:

- Mantenha `Task`s atômicas e testáveis.
- Use `outputs` versionados para artefatos reprodutíveis.
- Versione o `manifest` junto ao código que o gera.
