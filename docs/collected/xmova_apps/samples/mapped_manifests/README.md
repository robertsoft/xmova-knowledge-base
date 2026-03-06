README — mapped_manifests

Origem
- Contém manifests gerados automaticamente a partir de uma varredura dos projetos em `C:/dev/projects/xMova Apps` usando heurísticas e regras implementadas em `scripts/map_blocks_to_manifest.py`.

Resumo
- Total gerado: 3.944 manifests (arquivo compactado: `mapped_manifests.zip`).
- Objetivo: fornecer exemplos e ponto de partida para integração com pipelines e análise.

Avisos
- Arquivos gerados automaticamente — exigem revisão manual antes de uso em produção.
- Nem todas as associações de `inputs/outputs` ou `resources` foram resolvidas semanticamente; trate como rascunho automatizado.

Como validar um manifesto
```bash
python scripts/validate_manifests_batch.py docs/collected/xmova_apps/samples/mapped_manifests/
```

Como usar estes arquivos com o Copilot
- Abra o workspace `xmova.code-workspace` ou abra `C:/xmova-knowledge-base` junto com o projeto em que trabalha; mantenha este README e `examples/starter-templates/manifest-example.yaml` abertos para fornecer contexto.

Contato
- Para dúvidas ou revisão manual, abra uma issue ou PR referenciando `xmova/mapped-manifests`.
