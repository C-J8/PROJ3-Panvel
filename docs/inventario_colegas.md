# Inventario do Material dos Colegas

Material analisado em `Colegas/repositorio_colegas/metas_panvel-main/`.

## O que fica como referencia

### Arthur

Arquivo:

- `notebooks/eda_aa/eda_arthur_demo.ipynb`

Contribuicoes:

- analise de metas `MED` vs `N-MED`;
- metas zeradas;
- vendas sem meta;
- quantidade de filiais com historico completo;
- datas comerciais, feriados e Black Friday;
- devolucoes analisadas separadamente de vendas.

Uso recomendado:

- levar achados de qualidade para uma etapa `01_eda_qualidade`;
- reaproveitar logica de datas comerciais depois da base de modelagem inicial.

### Gustavo

Arquivos:

- `notebooks/eda_gl/eda_gustavo_demo.ipynb`
- `notebooks/eda_gl/feature_engineering_demo.ipynb`

Contribuicoes:

- ticket medio por filial;
- faturamento total por filial;
- graficos temporais de vendas;
- ideia de features de modelagem: dia da semana, mes, fim de semana, lags e medias moveis;
- encoding simples de variaveis binarias de filial.

Uso recomendado:

- reaproveitar principalmente em `04_base_modelagem`.

### Celso

Arquivos:

- `notebooks/eda_cj/eda_cj_demo.ipynb`
- `notebooks/eda_cj/Preparacao_bases_demo.ipynb`
- `notebooks/eda_cj/Bases_cluster_demo.ipynb`
- `notebooks/eda_cj/Clusterizacao_demo.ipynb`

Contribuicoes:

- esqueleto principal da pipeline atual;
- preparacao da `Base_V1`;
- separacao da `Base_exo`;
- construcao da `Base_V2`;
- clusterizacao de filiais.

Observacao:

- os tres notebooks principais do `eda_cj` sao iguais aos notebooks oficiais movidos para `notebooks/01_pipeline_atual/`.
- os Parquets dentro do repo dos colegas parecem versoes anteriores/regravadas; os arquivos atuais em `Base_V2/` devem ser tratados como referencia mais nova.

### BC / DuckDB

Pasta:

- `notebooks/eda_bc/`

Contribuicoes:

- organizacao por queries e CLI de EDA;
- relatorios e graficos;
- analise de performance vendas vs meta;
- analise de devolucoes e picos trimestrais;
- scripts de seeds para feriados e dados demograficos.

Decisao atual:

- nao usar o SQL diretamente na pipeline oficial por enquanto.
- manter as ideias como referencia, especialmente feriados, dados demograficos, devolucoes e performance mensal.

## Dados duplicados

Os Parquets em `Colegas/dados_panvel_duplicados/` foram comparados com `Base_Origi/` e sao iguais. Eles ficam preservados, mas a pipeline deve ler `Base_Origi/`.

## Dados externos

- `Colegas/dados_externos/municipios/`: shapefile de municipios.
- `Colegas/dados_externos/cnes/`: bases CNES 2024 e 2025.

Uso recomendado:

- nao entram na primeira versao da modelagem.
- podem ser avaliados depois como enriquecimento externo.
