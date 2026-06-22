# Features

Notebook oficial:

1. `01_features_base_v2.ipynb`

Objetivo:

- ler `Base_V1/`;
- gerar features diarias por filial;
- gerar features agregadas por filial;
- consolidar features uteis dos colegas, como dia util, lags e medias moveis;
- reaproveitar o padrao de calendario criado na preparacao, incluindo `dia_semana_id` e `fim_semana_id`;
- salvar as bases oficiais em `Base_V2/`.

## Saidas

| Arquivo | Uso |
|---|---|
| `Base_V2/features_filiais_diarias_V2.parquet` | Base diaria principal para modelagem. |
| `Base_V2/features_filiais_agregadas_V2.parquet` | Perfil consolidado por filial, usado para analise e diagnostico. |

## Decisao Atual

A etapa de clusterizacao saiu da pipeline oficial. Seguimos direto para a modelagem com CatBoost e LightGBM usando a base diaria.

Execute a partir da raiz do repositorio para manter `Path.cwd()` correto.
