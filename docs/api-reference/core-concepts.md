# Conceitos Principais da xmova

Este documento descreve os conceitos fundamentais da tecnologia proprietária xmova, servindo como referência rápida para desenvolvedores, revisores e agentes automatizados.

## Visão Geral
xmova é uma plataforma modular para processamento de pipelines de dados e execução de modelos, projetada para integração com agentes e fluxos automatizados.

## Componentes Principais
- xmova-core: Biblioteca central que orquestra pipelines e gerencia estados.
- xmova-runtime: Ambiente de execução responsável por instanciar e escalonar tarefas.
- xmova-sdk: Conjunto de utilitários e bindings para integrar aplicações com xmova.
- xmova-agent: Camada destinada a agentes (humanos ou IA) que interagem com a plataforma para automação e manutenção.

## Modelo de Dados
- Entidades principais: `Job`, `Task`, `Artifact`, `Pipeline`, `Run`.
- `Job`: unidade lógica de trabalho (ex.: transformar dataset A em B).
- `Task`: passo atômico dentro de um `Job`.

## Padrões de Interação
- Declarativo: pipelines são descritos por manifestos versionados.
- Imutabilidade: artifacts produzidos são imutáveis e versionados.
- Observabilidade: cada `Run` gera logs e métricas vinculadas ao `Job`.

## API e Extensibilidade
- Pontos de extensão: hooks de pré/post-task, adaptadores de storage, conectores de modelo.
- SDK oferece: criação/validação de pipelines, execução síncrona/assíncrona, consulta de runs.

## Exemplos Rápidos
- Criar um `Job` mínimo: definir `Pipeline` com 2 `Task`s (ingestão, transformação).
- Executar localmente via `xmova-runtime --run <manifest>`.

## Boas Práticas
- Mantenha `Task`s pequenas e testáveis.
- Versione manifestos junto ao código que os produz.
- Use `Artifact` imutáveis para facilitar reprodutibilidade.

## Próximos passos sugeridos
- Documentar o formato de manifesto (schema).
- Adicionar exemplos concretos em `/examples/starter-templates`.
- Expandir o glossário em `.github/agents/xmova-expert.md`.

