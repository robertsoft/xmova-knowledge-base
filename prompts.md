# Prompts prontos para GitHub Copilot

Este arquivo contém exemplos reais (representativos) e templates prontos para usar com o Copilot quando estiver trabalhando em projetos `.xmv` dentro do workspace que inclui `xmova-knowledge-base`.

---

## Exemplo 1 — `recorddetail` simples → manifesto

Entrada (.xmv):

```
recorddetail CustomerDetail {
  fields:
    name: customer_name
    id: customer_id
  query: "SELECT id, name FROM customers WHERE active = 1"
}
```

Prompt (use no topo do arquivo onde implementa a função):

```
Use xmova-knowledge-base as reference (manifest-schema.json + examples).
Entrada .xmv:
<cole o trecho acima>
Saída esperada: YAML de manifesto com um `pipeline.tasks` que contém:
- id: "customer-detail"
- resources: a query como um resource/statement
- outputs: campos `id` e `name` como outputs (lista de objetos {name: ...})
Escreva a função Python `map_sample_to_manifest(xmv_text)` que retorne um dicionário pronto para dump em YAML.
```

Saída de exemplo (manifest YAML resumido):

```yaml
apiVersion: xmova/v1
kind: Manifest
metadata:
  name: customer-detail-manifest
pipeline:
  tasks:
    - id: customer-detail
      type: query
      resources:
        - name: customers_query
          type: sql
          query: "SELECT id, name FROM customers WHERE active = 1"
      outputs:
        - name: id
        - name: name
```

---

## Exemplo 2 — `recordlist` com mapeamento para múltiplas tasks

Entrada (.xmv):

```
recordlist OrdersList {
  columns: order_id, total, status
  source: "SELECT order_id, total, status FROM orders WHERE status IN ('open','pending')"
  postprocess: "compute_tax(total)"
}
```

Prompt:

```
Converter este bloco `.xmv` em um manifesto com duas tasks:
1) `fetch-orders` que executa a query (resource SQL)
2) `compute-tax` que recebe `total` como input e produz `tax_amount` como output
Garantir que `pipeline.tasks[*].id` exista e `outputs` seja lista de objetos {name: ...}.
```

Saída de exemplo (resumida):

```yaml
pipeline:
  tasks:
    - id: fetch-orders
      type: query
      resources:
        - name: orders_query
          type: sql
          query: "SELECT order_id, total, status FROM orders WHERE status IN ('open','pending')"
      outputs:
        - name: order_id
        - name: total
        - name: status
    - id: compute-tax
      type: transform
      inputs:
        - from: fetch-orders.total
      outputs:
        - name: tax_amount
```

---

## Exemplo 3 — Hook / evento simples

Entrada (.xmv):

```
on_success notify_admin {
  message: "Order processed: {order_id}"
  to: admin@example.com
}
```

Prompt:

```
Gere uma entrada `hooks` no manifesto que represente o `on_success notify_admin` com campos `message` e `to`.
Mostre também como vincular o hook ao task que produz `order_id` (ex.: `fetch-orders`).
```

Saída de exemplo:

```yaml
hooks:
  - event: on_success
    name: notify_admin
    params:
      message: "Order processed: {order_id}"
      to: admin@example.com
# Exemplo de ligação: adicionar `on_success: notify_admin` no task `process-order`
```

---

## Templates / Prompts rápidos (prontos para colar)

1) Mapeamento simples:

```
# Use xmova-knowledge-base as reference (manifest-schema.json + examples)
# Entrada .xmv:
# <cole aqui>
# Saída: manifesto YAML compatível com schema
def map_sample_to_manifest(xmv_text):
    """Converter .xmv em manifesto (dicionário)."""
```

2) Validação após mapeamento:

```
# Converter e validar
manifest = map_sample_to_manifest(xmv_text)
# Em seguida, validar contra manifest-schema.json
# Retornar (manifest, errors)
```

3) Gerar testes `pytest`:

```
# Criar fixtures a partir de exemplos em xmova-knowledge-base/examples
# Escrever 3 testes: válido, campo obrigatório faltando, outputs malformados
```

4) Pedir melhoria heurística:

```
# Analise scripts/map_blocks_to_manifest.py e sugira 5 heurísticas para reduzir falsos positivos.
```

---

## Como usar

- Cole o prompt no topo do arquivo em que você trabalha (ou em um comentário) e invoque o Copilot.
- Mantenha abertos `docs/schema/manifest-schema.json` e `examples/starter-templates/manifest-example.yaml` para contexto.
- Valide automaticamente com `python scripts/validate_manifests_batch.py <diretório>`.

---

Se quiser, eu atualizo o arquivo `prompts.md` com exemplos retirados diretamente de amostras reais coletadas (se você autorizar o uso de trechos dos seus códigos).