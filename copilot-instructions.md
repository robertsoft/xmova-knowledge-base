# GitHub Copilot — instruções para o conjunto xmova-knowledge-base

Objetivo
- Fornecer ao GitHub Copilot contexto prioritário e exemplos para gerar transformações e assistências relacionadas ao DSL `.xmv` e ao formato de manifesto (`manifest-schema.json`).

Arquivos de referência (abra-os no VS Code quando for trabalhar)
- `docs/schema/manifest-schema.json` — esquema de validação do manifesto
- `examples/starter-templates/manifest-example.yaml` — exemplo de manifesto
- `scripts/map_blocks_to_manifest.py` — heurísticas de mapeamento (exemplo de implementação)
- `docs/collected/xmova_apps/samples/mapped_manifests/` — artefatos gerados (uso como referência)

Como usar (fluxo recomendado)
1. Abra o workspace multi-root `xmova.code-workspace` (inclui a knowledge-base e a pasta de apps).
2. Abra o arquivo `.xmv` que está mantendo e, ao mesmo tempo, mantenha abertos os arquivos de referência listados acima.
3. No arquivo onde quer implementar a conversão, cole um exemplo pequeno de entrada `.xmv` e o manifesto esperado como comentário no topo.
4. Escreva a assinatura da função (ex.: `def map_sample_to_manifest(xmv_text):`) e invoque o Copilot; ele usará os exemplos abertos para sugerir a implementação.

Prompts e exemplos de comentários para usar com Copilot
- "Use `xmova-knowledge-base/docs/schema/manifest-schema.json` como referência para gerar um manifesto válido." 
- Comentário de entrada/saída sugerido:
  ```py
  # Entrada .xmv:
  # <cole aqui trecho .xmv>
  # Saída esperada: YAML de manifesto compatível com manifest-schema.json
  def map_sample_to_manifest(xmv_text):
      ...
  ```

Comandos úteis
- Re-gerar manifests para um projeto e validar as saídas:
```bash
python scripts/map_all_repo_xmv.py --input "C:/dev/projects/xMova Apps/<App>" --out docs/collected/xmova_apps/samples/mapped_manifests/
python scripts/validate_manifests_batch.py docs/collected/xmova_apps/samples/mapped_manifests/
```
- Abrir projeto com knowledge-base (PowerShell):
```powershell
cd C:/xmova-knowledge-base/scripts
./open-xmova.ps1 -ProjectPath "MyApp"
```

Boas práticas
- Mantenha 3–5 exemplos representativos abertos para o Copilot generalizar melhor.
- Sempre valide automaticamente as saídas geradas usando `validate_manifests_batch.py`.
- Se o Copilot sugerir algo incerto, peça explicitamente: "Priorize exemplos em xmova-knowledge-base".

Observações
- Este arquivo fica centralizado em `xmova-knowledge-base`; não é necessário copiá-lo para cada projeto.
- Recomenda-se incluir este workspace (ou abrir a knowledge-base) sempre que for trabalhar em apps `.xmv` para que o Copilot use esse corpus como contexto prioritário.
