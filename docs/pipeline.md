# Pipeline Oficial

Este documento organiza o que foi feito no projeto em uma sequencia reproduzivel. O material util dos colegas foi movido para `notebooks/00_referencias/`, `reports/`, `assets/`, `src/` e `dados_externos/`. A pipeline oficial deve partir dos notebooks ordenados e, depois, migrar a logica para `src/`.

## 00. Referencias de EDA

Objetivo: manter os materiais individuais de EDA como memoria e fonte de consulta.

Fontes:

- `notebooks/00_referencias/colegas/arthur/eda_arthur_demo.ipynb`
- `notebooks/00_referencias/colegas/gustavo/eda_gustavo_demo.ipynb`
- `notebooks/00_referencias/colegas/gustavo/feature_engineering_demo.ipynb`
- `notebooks/00_referencias/colegas/celso/eda_cj_demo.ipynb`
- `notebooks/00_referencias/colegas/bc/`
- `reports/eda_bc/`

Pontos que entram como referencia:

- qualidade das metas e metas zeradas;
- vendas sem meta;
- historico completo por filial;
- perfil das filiais;
- ticket medio e faturamento por filial;
- ideias de lags e medias moveis;
- devolucoes como diagnostico separado.

## 01. EDA Consolidado

Notebook oficial:

- `notebooks/01_eda/01_eda_consolidado.ipynb`

Objetivo:

- juntar os principais achados de EDA do grupo;
- conferir qualidade e consistencia das bases;
- documentar decisoes para preparacao, features e modelagem;
- evitar que a leitura oficial do projeto dependa de varios notebooks soltos.

## 02. Preparacao da Base V1

Notebook oficial:

- `notebooks/02_preparacao/01_preparacao_base_v1.ipynb`

Entradas:

- `Base_Origi/project-puc_vendas.parquet`
- `Base_Origi/project-puc_metas.parquet`
- `Base_Origi/project-puc_filiais.parquet`
- `Base_Origi/project-puc_filiais_dt_abertura.parquet`
- `Base_Origi/project-puc_devolucoes.parquet`

Responsabilidades:

- padronizar datas e tipos;
- remover ou tratar a filial `1704` quando aplicavel;
- criar `vendas_diaria`;
- separar filiais jovens/fora do escopo em `Base_exo`;
- salvar a camada `Base_V1`.

Saidas:

- `Base_V1/filiais_V1.parquet`
- `Base_V1/metas_V1.parquet`
- `Base_V1/vendas_V1.parquet`
- `Base_V1/vendas_diaria_V1.parquet`
- `Base_exo/*.parquet`

## 03. Features da Base V2

Notebook oficial:

- `notebooks/03_features/01_features_base_v2.ipynb`

Entradas:

- `Base_V1/*.parquet`

Responsabilidades:

- criar features diarias por filial;
- criar features agregadas por filial;
- consolidar features uteis dos colegas, como flags de dia util, lags, medias moveis e cadastro expandido;
- calcular padroes por semana do mes e dia da semana;
- gerar ratios de calendario para diagnostico e features auxiliares;
- salvar as bases de features usadas pela modelagem.

Saidas:

- `Base_V2/features_filiais_diarias_V2.parquet`
- `Base_V2/features_filiais_agregadas_V2.parquet`

## 04. Base de Modelagem

Status: primeira versao implementada.

Pasta:

- `notebooks/05_modelagem/`

Entrada:

- `Base_V2/features_filiais_diarias_V2.parquet`
- `docs/features_consolidacao.md`

Responsabilidades:

- definir alvo principal como faturamento bruto;
- selecionar lags, medias moveis e features calendario ja criadas na V2;
- remover variaveis com vazamento de informacao;
- separar treino, validacao e teste por tempo.

Saidas:

- `Base_Modelagem/base_modelagem_diaria.parquet`
- `Base_Modelagem/features_modelagem.json`

## 05. Modelagem

Status: primeira versao implementada com CatBoost e LightGBM.

Responsabilidades:

- baseline simples;
- modelos globais por filial-dia;
- CatBoost e LightGBM;
- avaliacao temporal por filial, categoria e mes.

Saidas:

- `Base_Modelagem/predicoes_catboost_lightgbm.parquet`
- `Base_Modelagem/metricas_catboost_lightgbm.parquet`
- `Base_Modelagem/importancias_catboost_lightgbm.parquet`

## Regra de Execucao

Os notebooks atuais usam caminhos relativos ao diretorio raiz do projeto. Execute o Jupyter a partir da raiz `PROJ3- Panvel` para que `Path.cwd()` aponte para o lugar esperado.
