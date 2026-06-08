# Pipeline Oficial

Este documento organiza o que foi feito no projeto em uma sequencia reproduzivel. A pasta `Colegas/` continua como memoria bruta do trabalho dos colegas; a pipeline oficial deve partir dos notebooks e, depois, migrar a logica para `src/`.

## 00. Referencias e EDA

Objetivo: concentrar os achados exploratorios antes de transformar em regra de pipeline.

Fontes:

- `Colegas/repositorio_colegas/metas_panvel-main/notebooks/eda_aa/eda_arthur_demo.ipynb`
- `Colegas/repositorio_colegas/metas_panvel-main/notebooks/eda_gl/eda_gustavo_demo.ipynb`
- `Colegas/repositorio_colegas/metas_panvel-main/notebooks/eda_gl/feature_engineering_demo.ipynb`
- `Colegas/repositorio_colegas/metas_panvel-main/notebooks/eda_cj/eda_cj_demo.ipynb`
- `Colegas/repositorio_colegas/metas_panvel-main/notebooks/eda_bc/`

Pontos que entram como referencia:

- qualidade das metas e metas zeradas;
- vendas sem meta;
- historico completo por filial;
- perfil das filiais;
- ticket medio e faturamento por filial;
- ideias de lags e medias moveis;
- devolucoes como diagnostico separado.

## 01. Preparacao da Base V1

Notebook oficial:

- `notebooks/01_pipeline_atual/01_preparacao_base_v1.ipynb`

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

## 02. Features da Base V2

Notebook oficial:

- `notebooks/01_pipeline_atual/02_features_base_v2.ipynb`

Entradas:

- `Base_V1/*.parquet`

Responsabilidades:

- criar features diarias por filial;
- criar features agregadas por filial;
- calcular padroes por semana do mes e dia da semana;
- gerar ratios de calendario;
- preparar matrizes de clusterizacao.

Saidas:

- `Base_V2/features_filiais_diarias_V2.parquet`
- `Base_V2/features_filiais_agregadas_V2.parquet`
- `Base_V2/features_filiais_cluster_semana_dia_V2.parquet`

## 03. Clusterizacao de Filiais

Notebook oficial:

- `notebooks/01_pipeline_atual/03_clusterizacao_filiais.ipynb`

Entradas:

- `Base_V2/features_filiais_cluster_semana_dia_V2.parquet`
- `Base_V2/features_filiais_diarias_V2.parquet`

Responsabilidades:

- testar configuracoes de clusterizacao;
- escolher uma referencia interpretavel;
- gerar perfil dos clusters;
- validar os clusters na base diaria.

Saidas:

- `Base_V2/cluster_filial_modelagem_V2.parquet`
- `Base_V2/perfil_clusters_V2.parquet`

## 04. Base de Modelagem

Status: proxima etapa.

Entrada sugerida:

- `Base_V2/features_filiais_diarias_V2.parquet`
- `Base_V2/cluster_filial_modelagem_V2.parquet`
- ideias de `Colegas/repositorio_colegas/metas_panvel-main/notebooks/eda_gl/feature_engineering_demo.ipynb`

Responsabilidades:

- definir alvo principal como faturamento bruto;
- criar lags e medias moveis;
- adicionar features calendario permitidas;
- remover variaveis com vazamento de informacao;
- separar treino, validacao e teste por tempo.

Saidas planejadas:

- `Base_Modelagem/base_modelagem_diaria.parquet`

## 05. Modelagem

Status: proxima etapa.

Responsabilidades:

- baseline simples;
- modelos por categoria `MED` e `N-MED`;
- teste com cluster como feature ou segmentacao;
- avaliacao temporal por filial, categoria e mes.

## Regra de Execucao

Os notebooks atuais usam caminhos relativos ao diretorio raiz do projeto. Execute o Jupyter a partir da raiz `PROJ3- Panvel` para que `Path.cwd()` aponte para o lugar esperado.
