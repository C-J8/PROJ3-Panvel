# Modelagem

Esta pasta contem a primeira versao da modelagem diaria de faturamento bruto por filial.

## Notebooks

1. `01_base_modelagem_diaria.ipynb`
2. `02_catboost_lightgbm.ipynb`

## Decisoes

- Alvo principal: `faturamento_bruto_dia`.
- Granularidade: uma linha por `codigo_filial` e `data`.
- Modelagem inicial sem clusterizacao.
- Modelos globais treinados com todas as filiais juntas.
- CatBoost e LightGBM treinados em `target_log1p`.
- Predicoes convertidas de volta para reais com `expm1`.

## Split Temporal

| Conjunto | Periodo |
|---|---|
| Treino | ate 2025-08-31 |
| Validacao | 2025-09-01 a 2025-10-31 |
| Teste | 2025-11-01 a 2025-12-31 |

## Cuidados Contra Vazamento

Ficam fora da base inicial:

- variaveis do proprio dia, como `cupons_dia`, `quantidade_dia`, `ticket_medio_bruto_dia` e shares do dia;
- quebras MED/N-MED do proprio dia;
- perfis temporais calculados com a serie completa;
- agregados historicos completos da filial calculados usando todo o periodo.

Entram na base:

- calendario;
- dia util e feriados;
- cadastro da filial;
- lags;
- medias moveis com `shift(1)`;
- idade e metragem da filial.

## Saidas

- `Base_Modelagem/base_modelagem_diaria.parquet`
- `Base_Modelagem/features_modelagem.json`
- `Base_Modelagem/predicoes_catboost_lightgbm.parquet`
- `Base_Modelagem/metricas_catboost_lightgbm.parquet`
- `Base_Modelagem/importancias_catboost_lightgbm.parquet`

## Resultado Inicial

No conjunto de teste, o melhor modelo inicial foi o LightGBM:

| Modelo | WAPE teste | MAE teste |
|---|---:|---:|
| LightGBM | 19,55% | 17.703,65 |
| CatBoost | 20,58% | 18.630,17 |
| Media movel 28d | 27,73% | 25.110,56 |
| Lag 7d | 31,54% | 28.556,91 |
