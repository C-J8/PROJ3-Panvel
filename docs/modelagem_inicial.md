# Modelagem Inicial

Este documento resume a primeira versao da modelagem diaria de faturamento bruto por filial.

## Arquivos

- `notebooks/05_modelagem/01_base_modelagem_diaria.ipynb`
- `notebooks/05_modelagem/02_catboost_lightgbm.ipynb`
- `Base_Modelagem/base_modelagem_diaria.parquet`
- `Base_Modelagem/features_modelagem.json`
- `Base_Modelagem/predicoes_catboost_lightgbm.parquet`
- `Base_Modelagem/metricas_catboost_lightgbm.parquet`
- `Base_Modelagem/importancias_catboost_lightgbm.parquet`

## Estrategia

A modelagem inicial usa modelos globais, com todas as filiais na mesma base. A clusterizacao ficou fora desta primeira rodada.

Foram comparados:

- baseline `lag_7d`;
- baseline `media_movel_28d`;
- CatBoost;
- LightGBM.

O alvo e `faturamento_bruto_dia`. CatBoost e LightGBM foram treinados em `target_log1p`, e as predicoes voltaram para reais com `expm1`.

## Split Temporal

| Conjunto | Periodo | Linhas |
|---|---|---:|
| Treino | ate 2025-08-31 | 60.882 |
| Validacao | 2025-09-01 a 2025-10-31 | 6.100 |
| Teste | 2025-11-01 a 2025-12-31 | 6.100 |

## Resultado

| Modelo | Conjunto | WAPE | MAE | RMSE | Bias |
|---|---|---:|---:|---:|---:|
| LightGBM | Teste | 19,55% | 17.703,65 | 35.853,37 | -8,73% |
| CatBoost | Teste | 20,58% | 18.630,17 | 39.396,85 | -8,91% |
| Media movel 28d | Teste | 27,73% | 25.110,56 | 43.861,93 | 0,52% |
| Lag 7d | Teste | 31,54% | 28.556,91 | 54.722,91 | 2,54% |

## Observacoes

- LightGBM foi o melhor modelo inicial no teste.
- CatBoost tambem superou os baselines, mas ficou abaixo do LightGBM.
- Ambos os modelos apresentaram viés negativo no teste, subestimando o faturamento total.
- A proxima iteracao deve investigar calibracao, avaliacao por filial e validacao temporal mais robusta.
