# Modelagem Inicial

Este documento resume a primeira versão da modelagem diária de faturamento bruto por filial.

## Arquivos

- `notebooks/05_modelagem/01_base_modelagem_diaria.ipynb`
- `notebooks/05_modelagem/02_catboost_lightgbm.ipynb`
- `notebooks/05_modelagem/03_importancia_features_e_meses.ipynb`
- `Base_Modelagem/base_modelagem_diaria.parquet`
- `Base_Modelagem/features_modelagem.json`
- `Base_Modelagem/predicoes_catboost_lightgbm.parquet`
- `Base_Modelagem/metricas_catboost_lightgbm.parquet`
- `Base_Modelagem/importancias_catboost_lightgbm.parquet`
- `Base_Modelagem/importancia_permutation_lightgbm.parquet`
- `Base_Modelagem/importancia_grupos_lightgbm.parquet`
- `Base_Modelagem/importancia_shap_lightgbm.parquet`
- `Base_Modelagem/metricas_janelas_mensais.parquet`
- `Base_Modelagem/predicoes_janelas_mensais.parquet`

## Estratégia

A modelagem inicial usa modelos globais, com todas as filiais na mesma base. A clusterização ficou fora desta primeira rodada.

Foram comparados:

- baseline `lag_7d`;
- baseline `media_movel_28d`;
- CatBoost;
- LightGBM.

O alvo é `faturamento_bruto_dia`. CatBoost e LightGBM foram treinados em `target_log1p`, e as predições voltaram para reais com `expm1`.

## Split Temporal

| Conjunto | Período | Linhas |
|---|---|---:|
| Treino | até 2025-08-31 | 60.882 |
| Validação | 2025-09-01 a 2025-10-31 | 6.100 |
| Teste | 2025-11-01 a 2025-12-31 | 6.100 |

## Resultado

| Modelo | Conjunto | WAPE | MAE | RMSE | Bias |
|---|---|---:|---:|---:|---:|
| LightGBM | Teste | 19,55% | 17.703,65 | 35.853,37 | -8,73% |
| CatBoost | Teste | 20,58% | 18.630,17 | 39.396,85 | -8,91% |
| Média móvel 28d | Teste | 27,73% | 25.110,56 | 43.861,93 | 0,52% |
| Lag 7d | Teste | 31,54% | 28.556,91 | 54.722,91 | 2,54% |

## Diagnósticos Adicionais

O notebook `03_importancia_features_e_meses.ipynb` adiciona análises replicáveis para:

- importância de features no LightGBM por importância nativa, permutation importance e SHAP;
- importância por grupo de features;
- comparação de janelas históricas de 2024 para prever cada mês de 2025.

## Observações

- LightGBM foi o melhor modelo inicial no teste.
- CatBoost também superou os baselines, mas ficou abaixo do LightGBM.
- Ambos os modelos apresentaram viés negativo no teste, subestimando o faturamento total.
- A próxima iteração deve investigar calibração, avaliação por filial e validação temporal mais robusta.
