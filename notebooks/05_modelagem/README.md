# Modelagem

Esta pasta contém a primeira versão da modelagem diária de faturamento bruto por filial.

## Notebooks

1. `01_base_modelagem_diaria.ipynb`
2. `02_catboost_lightgbm.ipynb`
3. `03_importancia_features_e_meses.ipynb`

## Ambiente

Para reproduzir a modelagem e os diagnósticos, instale as dependências com:

```bash
pip install -r requirements-modelagem.txt
```

## Decisões

- Alvo principal: `faturamento_bruto_dia`.
- Granularidade: uma linha por `codigo_filial` e `data`.
- Modelagem inicial sem clusterização.
- Modelos globais treinados com todas as filiais juntas.
- CatBoost e LightGBM treinados em `target_log1p`.
- Predições convertidas de volta para reais com `expm1`.

## Split Temporal

| Conjunto | Período |
|---|---|
| Treino | até 2025-08-31 |
| Validação | 2025-09-01 a 2025-10-31 |
| Teste | 2025-11-01 a 2025-12-31 |

## Cuidados Contra Vazamento

Ficam fora da base inicial:

- variáveis do próprio dia, como `cupons_dia`, `quantidade_dia`, `ticket_medio_bruto_dia` e shares do dia;
- quebras MED/N-MED do próprio dia;
- perfis temporais calculados com a série completa;
- agregados históricos completos da filial calculados usando todo o período.

Entram na base:

- calendário;
- dia útil e feriados;
- cadastro da filial;
- lags;
- médias móveis com `shift(1)`;
- idade e metragem da filial.

## Saídas

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

## Diagnósticos Replicáveis

O notebook `03_importancia_features_e_meses.ipynb` adiciona duas leituras complementares:

- importância de features no LightGBM por importância nativa, permutation importance e SHAP;
- teste de janelas mensais, comparando quais meses de 2024 ajudam mais a prever cada mês de 2025.

No teste de janelas mensais, as features de lag e média móvel são removidas para isolar melhor o efeito do histórico mensal usado no treino.

## Resultado Inicial

No conjunto de teste, o melhor modelo inicial foi o LightGBM:

| Modelo | WAPE teste | MAE teste |
|---|---:|---:|
| LightGBM | 19,55% | 17.703,65 |
| CatBoost | 20,58% | 18.630,17 |
| Média móvel 28d | 27,73% | 25.110,56 |
| Lag 7d | 31,54% | 28.556,91 |
