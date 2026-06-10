# EDA Consolidado

Este diretorio contem a analise exploratoria oficial do projeto Panvel. O objetivo e reunir, em uma leitura unica, os principais achados produzidos pelo grupo e transformar os notebooks individuais em decisoes praticas para a pipeline.

## Notebook Oficial

- `01_eda_consolidado.ipynb`

O notebook deve ser executado a partir da raiz do repositorio `PROJ3- Panvel`, pois os caminhos usam `Path.cwd()` como referencia.

## Objetivo da Analise

A EDA consolidada responde quatro perguntas principais:

1. As bases recebidas estao consistentes em volume, datas, filiais e chaves?
2. Quais filiais entram no escopo principal de modelagem e quais ficam em analise separada?
3. O faturamento deve ser tratado como bruto ou liquido?
4. Quais pontos precisam ser tratados antes de features, clusterizacao e modelagem?

## Fontes Consideradas

Materiais consolidados:

- bases originais em `Base_Origi/`;
- bases preparadas em `Base_V1/`, `Base_V2/` e `Base_exo/`;
- EDAs individuais preservados em `notebooks/00_referencias/`;
- relatorios e graficos do BC em `reports/eda_bc/`;
- checagem formal em `reports/data_quality.md`.

## Principais Decisoes

- O alvo principal do projeto sera `faturamento_bruto`.
- Devolucoes e faturamento liquido ficam como diagnostico ou possiveis variaveis auxiliares, nao como alvo inicial.
- A filial `1704` fica fora da base oficial porque aparece nas transacoes, mas nao possui cadastro confiavel.
- A `Base_V1` concentra as 100 filiais elegiveis para features, clusterizacao e modelagem.
- A `Base_exo` preserva 24 filiais jovens ou fora do escopo principal atual.
- Metas zeradas e datas ausentes devem ser tratadas explicitamente antes da modelagem.

## Saidas Esperadas

Depois de revisar a EDA, a ordem recomendada e:

1. executar a preparacao da `Base_V1`;
2. gerar as features consolidadas da `Base_V2`;
3. executar a clusterizacao;
4. construir a base final de modelagem com validacao temporal.

## Documentos Relacionados

- `docs/pipeline.md`: ordem completa da pipeline.
- `reports/data_quality.md`: resultados da checagem de qualidade.
- `docs/faturamento.md`: decisao sobre bruto, liquido e devolucoes.
- `docs/features_consolidacao.md`: consolidacao das features vindas do grupo.
