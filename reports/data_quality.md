# Data Quality Check

Data da checagem: 2026-06-09.

## Cobertura de materiais

Os materiais de EDA/features preservados no projeto estao organizados em:

- `notebooks/02_preparacao/`: preparacao oficial da `Base_V1` e `Base_exo`.
- `notebooks/03_features/`: construcao oficial da `Base_V2`.
- `notebooks/04_clusterizacao/`: clusterizacao oficial das filiais.
- `notebooks/00_referencias/colegas/arthur/`: EDA do Arthur.
- `notebooks/00_referencias/colegas/gustavo/`: EDA e feature engineering do Gustavo.
- `notebooks/00_referencias/colegas/celso/`: EDA historico do Celso.
- `notebooks/00_referencias/colegas/bc/`: README do EDA estruturado BC.
- `reports/eda_bc/`: imagens e notas geradas pelo EDA BC.
- `src/data/`: loader/download e scripts externos reaproveitaveis.

O SQL do BC foi removido da arvore atual por decisao de pipeline: as ideias ficam documentadas, mas a implementacao oficial sera organizada pelos notebooks e modulos Python.

## Resumo das bases

| Base | Linhas | Colunas | Filiais distintas |
|---|---:|---:|---:|
| `Base_Origi/project-puc_filiais.parquet` | 124 | 10 | 124 |
| `Base_Origi/project-puc_filiais_dt_abertura.parquet` | 124 | 2 | 124 |
| `Base_Origi/project-puc_vendas.parquet` | 20.863.735 | 6 | 125 |
| `Base_Origi/project-puc_metas.parquet` | 81.268 | 5 | 125 |
| `Base_Origi/project-puc_devolucoes.parquet` | 85.677 | 5 | 125 |
| `Base_V1/filiais_V1.parquet` | 100 | 13 | 100 |
| `Base_V1/vendas_V1.parquet` | 19.565.924 | 7 | 100 |
| `Base_V1/metas_V1.parquet` | 73.099 | 6 | 100 |
| `Base_V1/vendas_diaria_V1.parquet` | 72.069 | 8 | 100 |
| `Base_exo/filiais_exo.parquet` | 24 | 13 | 24 |
| `Base_exo/vendas_exo.parquet` | 1.191.251 | 7 | 24 |
| `Base_exo/metas_exo.parquet` | 7.560 | 6 | 24 |
| `Base_exo/vendas_diaria_exo.parquet` | 7.301 | 8 | 24 |
| `Base_V2/features_filiais_diarias_V2.parquet` | 73.082 | 110 | 100 |
| `Base_V2/features_filiais_agregadas_V2.parquet` | 100 | 49 | 100 |
| `Base_V2/features_filiais_cluster_semana_dia_V2.parquet` | 100 | 196 | 100 |
| `Base_V2/cluster_filial_modelagem_V2.parquet` | 100 | 10 | 100 |
| `Base_V2/perfil_clusters_V2.parquet` | 4 | 18 | - |

## Consistencia de filiais

Resultado principal: a separacao atual bate.

- `Base_V1` tem 100 filiais.
- `Base_exo` tem 24 filiais.
- `Base_V1 + Base_exo` cobre exatamente as 124 filiais cadastradas em `Base_Origi/project-puc_filiais.parquet`.
- `Base_V1` e `Base_exo` nao se sobrepoem.
- `Base_V2` cobre exatamente as mesmas 100 filiais de `Base_V1`.
- A clusterizacao cobre exatamente as mesmas 100 filiais de `Base_V1`.

## Filial 1704

A filial `1704` aparece nas bases transacionais originais, mas nao aparece no cadastro de filiais nem na base de data de abertura.

| Base original | Linhas da filial `1704` | Periodo |
|---|---:|---|
| Vendas | 106.560 | 2024-01-01 a 2025-08-18 |
| Metas | 609 | 2024-01-01 a 2025-08-31 |
| Devolucoes | 495 | 2024-01-03 a 2025-08-14 |
| Filiais | 0 | - |
| Filiais data abertura | 0 | - |

Decisao atual: manter `1704` fora de `Base_V1` e `Base_exo`, pois falta cadastro para enriquecer/modelar corretamente.

## Datas

As bases originais principais cobrem 731 dias, de 2024-01-01 a 2025-12-31.

- Vendas original: 731 datas.
- Metas original: 731 datas.
- Devolucoes original: 731 datas.
- `Base_V1/vendas_V1`: 731 datas.
- `Base_V1/metas_V1`: 731 datas.
- `Base_V1/vendas_diaria_V1`: 731 datas.
- `Base_V2/features_filiais_diarias_V2`: 731 datas no conjunto total.

Observacoes:

- `Base_exo/vendas_exo` comeca em 2024-01-25, coerente com filiais jovens/fora do escopo principal.
- Em `Base_V2/features_filiais_diarias_V2`, 18 filiais tem 730 dias em vez de 731. Em todos os casos, a data ausente e 2024-01-01.
- Em `Base_V1/metas_V1`, a filial `1746` tem 730 dias; falta meta para 2024-02-04.

## Nulos e duplicatas

Nao foram encontrados nulos nas bases oficiais checadas:

- `Base_Origi`: filiais, filiais data abertura, metas, devolucoes e vendas.
- `Base_V1`: filiais, metas e vendas diaria.
- `Base_V2`: features diarias, agregadas e cluster.

Nao foram encontradas duplicatas nas chaves checadas:

- Filiais: `codigo_filial`.
- Filiais data abertura: `codigo_filial`.
- Metas: `codigo_filial + data_meta_venda`.
- Vendas diaria: `codigo_filial + data`.
- Features agregadas: `codigo_filial`.
- Cluster: `codigo_filial`.

## Metas

Pontos de atencao:

- Na base original, existem 1.491 linhas com `valor_meta_venda = 0`.
- Na base original, existem 62 linhas com `meta_med < 0`.
- Na `Base_V1`, nao ha metas negativas.
- Na `Base_V1`, ainda existem 1.126 linhas com `valor_meta_venda = 0`, em 25 filiais.
- Filiais com mais metas zeradas na `Base_V1`: `1509`, `1548`, `1500`, `1578`, `1590`, `1749`, `1734`, `1716`, `1599`, `1695`.

Decisao recomendada: antes da modelagem, tratar metas zeradas como caso especial. Elas podem representar ausencia de meta, loja fechada, feriado, dado operacional ou erro.

## Vendas e devolucoes

Vendas:

- `Base_Origi/project-puc_vendas.parquet`: faturamento total bruto de R$ 5.945.417.435,10.
- `Base_V1/vendas_V1.parquet`: faturamento total bruto de R$ 5.620.320.877,15.
- Nao foram encontrados valores negativos de faturamento ou quantidade em vendas.

Devolucoes na `Base_V1/vendas_diaria_V1`:

Existem 6 dias em que `valor_devolucao_dia > faturamento_bruto_dia`, gerando `faturamento_liquido_dia` negativo.

| Filial | Data | Faturamento bruto | Devolucao | Faturamento liquido |
|---|---|---:|---:|---:|
| 1671 | 2024-12-18 | 106.947,06 | 226.205,55 | -119.258,49 |
| 1665 | 2024-07-02 | 114.873,92 | 208.274,18 | -93.400,26 |
| 1776 | 2024-04-04 | 58.976,70 | 127.008,13 | -68.031,43 |
| 1563 | 2025-06-12 | 79.405,83 | 120.516,34 | -41.110,51 |
| 1608 | 2025-12-29 | 50.560,56 | 61.070,84 | -10.510,28 |
| 1536 | 2025-04-03 | 65.116,31 | 66.519,72 | -1.403,41 |

Decisao atual coerente: usar faturamento bruto como alvo principal e manter devolucoes/liquido como diagnostico ou feature auxiliar.

## Clusterizacao

`Base_V2/cluster_filial_modelagem_V2.parquet` cobre 100 filiais.

Distribuicao:

- `Intermediarias estaveis`: 81 filiais.
- `Alto volume e maior N-MED`: 7 filiais.
- `Menores sensiveis a dias uteis`: 11 filiais.
- `Atipica de alto volume`: 1 filial marcada como especial/outlier.

## Conclusao

A estrutura atual esta consistente para seguir para a proxima etapa.

Pontos que precisam entrar na preparacao da base de modelagem:

1. Decidir tratamento das 1.126 metas zeradas na `Base_V1`.
2. Investigar a meta ausente da filial `1746` em 2024-02-04.
3. Decidir se as 18 ausencias de 2024-01-01 na `Base_V2` devem ser preenchidas ou mantidas.
4. Manter `1704` fora da modelagem enquanto nao houver cadastro confiavel.
5. Usar faturamento bruto como alvo principal e tratar devolucoes como variavel auxiliar.
