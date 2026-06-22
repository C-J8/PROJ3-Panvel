# EDA - Projeto Panvel

Este diretorio contem a entrega consolidada da Analise Exploratoria de Dados (EDA) do projeto Panvel. O objetivo e reunir, em uma unica leitura, os principais achados sobre vendas, metas, devolucoes e cadastro de filiais, criando uma base clara para a etapa seguinte de features.

O material foi organizado para ser revisado de forma independente, inclusive em uma entrega compartilhada do grupo. Por isso, este README evita depender de contexto externo ao projeto e descreve o escopo, as entradas, as decisoes e a relacao da EDA com as proximas etapas.

## Arquivo Principal

- `01_eda_consolidado.ipynb`

Esse notebook consolida os achados exploratorios e registra as decisoes que orientam a preparacao da base e a criacao de features.

## Como Executar

Execute o Jupyter a partir da raiz do projeto, mantendo a estrutura de pastas abaixo:

```text
Base_Origi/
Base_V1/
Base_exo/
docs/
notebooks/
reports/
```

O notebook usa caminhos relativos ao diretorio raiz. Se ele for movido para outro repositorio, mantenha a mesma estrutura de pastas ou ajuste as variaveis de caminho nas primeiras celulas.

## Objetivos da EDA

A analise foi estruturada para responder:

1. Qual e a cobertura das bases em linhas, datas, filiais e colunas?
2. Existem divergencias entre o cadastro de filiais e as bases transacionais?
3. Quais filiais devem seguir para a base principal de modelagem?
4. Como tratar faturamento bruto, faturamento liquido e devolucoes?
5. Quais problemas precisam ser resolvidos antes da preparacao da base e da criacao de features?

## Bases Avaliadas

Entradas principais:

- `Base_Origi/project-puc_vendas.parquet`
- `Base_Origi/project-puc_metas.parquet`
- `Base_Origi/project-puc_filiais.parquet`
- `Base_Origi/project-puc_filiais_dt_abertura.parquet`
- `Base_Origi/project-puc_devolucoes.parquet`

Bases derivadas consideradas na validacao:

- `Base_V1/`
- `Base_exo/`

## Entregaveis da EDA

A EDA entrega uma leitura consolidada sobre:

- consistencia de filiais entre cadastro, vendas, metas e devolucoes;
- cobertura temporal das bases;
- qualidade das metas, incluindo casos zerados e negativos;
- diferencas entre faturamento bruto, devolucoes e faturamento liquido;
- separacao entre a base principal (`Base_V1`) e as filiais fora do escopo atual (`Base_exo`);
- pontos de atencao para a etapa de features.

## Decisoes Registradas

- O faturamento bruto foi definido como alvo principal inicial.
- Devolucoes e faturamento liquido devem ser mantidos como diagnostico ou variaveis auxiliares.
- A filial `1704` foi excluida da base oficial por nao possuir cadastro confiavel.
- A `Base_V1` concentra 100 filiais elegiveis para as etapas seguintes.
- A `Base_exo` preserva 24 filiais jovens ou fora do escopo principal.
- Metas zeradas e datas ausentes devem ser tratadas antes da modelagem.

## Handoff Para Features

A EDA fecha a etapa de entendimento e qualidade dos dados. A partir dela, a etapa de features deve usar:

- `Base_V1/` como fonte tratada principal;
- faturamento bruto como alvo inicial;
- devolucoes e faturamento liquido apenas como diagnostico ou variaveis auxiliares;
- `Base_exo/` fora do escopo principal, preservada para analises futuras;
- os pontos de qualidade registrados em `reports/data_quality.md` como checklist antes da modelagem.

O notebook responsavel pelas features oficiais e:

- `notebooks/03_features/01_features_base_v2.ipynb`

## Sequencia Recomendada

Depois de revisar a EDA, siga a ordem:

1. preparar a `Base_V1`;
2. gerar a base de features consolidada;
3. revisar a base de features antes de avancar para as etapas seguintes.

## Documentacao Complementar

Quando disponiveis no repositorio, os documentos abaixo complementam a EDA:

- `reports/data_quality.md`: checagem detalhada de qualidade das bases.
- `docs/faturamento.md`: decisao sobre faturamento bruto, liquido e devolucoes.
- `docs/pipeline.md`: ordem oficial das etapas do projeto.
