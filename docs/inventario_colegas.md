# Inventario do Material dos Colegas

Material originalmente recebido em `Colegas/repositorio_colegas/metas_panvel-main/` e reorganizado nas pastas oficiais do projeto.

## O que fica como referencia

### Arthur

Arquivo:

- `notebooks/00_referencias/colegas/arthur/eda_arthur_demo.ipynb`

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

- `notebooks/00_referencias/colegas/gustavo/eda_gustavo_demo.ipynb`
- `notebooks/00_referencias/colegas/gustavo/feature_engineering_demo.ipynb`
- `notebooks/00_referencias/colegas/gustavo/eda_gustavo.md`

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

- `notebooks/00_referencias/colegas/celso/eda_cj_demo.ipynb`
- `notebooks/02_preparacao/01_preparacao_base_v1.ipynb`
- `notebooks/03_features/01_features_base_v2.ipynb`
- `notebooks/04_clusterizacao/01_clusterizacao_filiais.ipynb`

Contribuicoes:

- esqueleto principal da pipeline atual;
- preparacao da `Base_V1`;
- separacao da `Base_exo`;
- construcao da `Base_V2`;
- clusterizacao de filiais.

Observacao:

- os tres notebooks principais do `eda_cj` eram iguais aos notebooks oficiais movidos para as pastas `notebooks/02_preparacao/`, `notebooks/03_features/` e `notebooks/04_clusterizacao/`.
- os Parquets dentro do repo dos colegas eram versoes anteriores/regravadas; os arquivos atuais em `Base_V2/` devem ser tratados como referencia mais nova.

### BC / DuckDB

Pasta:

- `notebooks/00_referencias/colegas/bc/`
- `reports/eda_bc/`

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

Os Parquets que estavam em `Colegas/dados_panvel_duplicados/` foram comparados com `Base_Origi/` e eram iguais. Eles foram removidos da arvore atual; a pipeline deve ler `Base_Origi/`.

## Dados externos

- `dados_externos/municipios/`: shapefile de municipios.
- `dados_externos/cnes/`: bases CNES 2024 e 2025.

Uso recomendado:

- nao entram na primeira versao da modelagem.
- podem ser avaliados depois como enriquecimento externo.

## Removido da arvore atual

- `Colegas/dados_panvel_duplicados/`: duplicata da `Base_Origi/`.
- `Colegas/dados_panvel_duplicados/arquivos_invalidos/project-puc_vendas (1).parquet`: arquivo vazio.
- `Colegas/zips_originais/metas_panvel-main.zip`: ZIP original ja extraido e reorganizado.
- SQLs do `eda_bc`: mantida apenas a documentacao/relatorios e scripts uteis; as queries nao entram na pipeline oficial.
- Parquets antigos dentro do `eda_cj`: substituidos pelos checkpoints atuais em `Base_V2/` e `Base_exo/`.
