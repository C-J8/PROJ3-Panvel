# Features Escolhidas

Este documento resume quais features foram escolhidas ate agora e onde elas estao implementadas.

## Notebook Principal

As features oficiais estao no notebook:

- `notebooks/03_features/01_features_base_v2.ipynb`

Esse notebook gera os arquivos:

- `Base_V2/features_filiais_diarias_V2.parquet`
- `Base_V2/features_filiais_agregadas_V2.parquet`

## Base Diaria Para Modelagem

Arquivo principal:

- `Base_V2/features_filiais_diarias_V2.parquet`

Grupos de features escolhidos:

| Grupo | Features |
|---|---|
| Calendario | `ano`, `mes`, `dia_mes`, `semana_mes`, `semana_ano`, `dia_semana_id`, `dia_semana`, `trimestre`, `semestre`, `eh_semana_5`, `fim_semana_id`, `eh_inicio_mes`, `eh_fim_mes`, `dias_no_mes` |
| Dia util | `eh_feriado_bancario`, `eh_dia_util`, `ordem_dia_util_mes`, `dias_uteis_no_mes`, `eh_primeiro_dia_util_mes`, `eh_quinto_dia_util_mes` |
| Cadastro da filial | `faixa_vida`, `localidade`, `uf`, `tipo_estabelecimento`, `delivery`, `metragem_area_venda`, `panvel_clinic`, `estacionamento`, `atendimento_24_horas`, `grupo_metragem`, `idade_filial_meses` |
| Historico de faturamento | `faturamento_bruto_lag_1d`, `faturamento_bruto_lag_7d`, `faturamento_bruto_lag_14d`, `faturamento_bruto_lag_28d`, `faturamento_bruto_media_movel_7d`, `faturamento_bruto_media_movel_28d`, `faturamento_bruto_std_movel_7d`, `faturamento_bruto_std_movel_28d` |
| Historico operacional | `cupons_lag_7d`, `quantidade_lag_7d`, `cupons_media_movel_28d`, `quantidade_media_movel_28d` |
| Historico MED/N-MED | `faturamento_med_lag_7d`, `faturamento_n_med_lag_7d`, `faturamento_med_media_movel_28d`, `faturamento_n_med_media_movel_28d`, `share_med_faturamento_lag_7d` |
| Perfil temporal da filial | `faturamento_bruto_ratio_mes_dia_semana`, `faturamento_bruto_media_mes_semana_dia`, `faturamento_bruto_cv_mes_semana_dia`, `faturamento_bruto_ratio_mes_semana_dia` |
| Perfil historico agregado | `dias_total`, `dias_com_venda_total`, `faturamento_bruto_medio_dia`, `faturamento_bruto_mediano_dia`, `cv_faturamento_bruto_dia`, `ticket_medio_bruto_dia_medio`, `itens_por_cupom_dia_medio`, `pct_dias_com_venda` |

## Variaveis Que Exigem Cuidado

Algumas colunas existem na base diaria, mas nao devem entrar automaticamente como features de previsao se o objetivo for prever faturamento antes do dia acontecer:

- `faturamento_bruto_dia`: alvo principal.
- `cupons_dia`, `quantidade_dia`, `ticket_medio_bruto_dia`, `itens_por_cupom_dia`: informacoes do proprio dia.
- `faturamento_med_dia`, `faturamento_n_med_dia`, `share_med_faturamento`, `share_n_med_faturamento`: tambem dependem do fechamento do dia.

Essas colunas podem ser usadas em EDA, diagnostico ou avaliacao posterior, mas precisam ser separadas na base de modelagem para evitar vazamento de informacao.

## Modelagem Atual

Notebook:

- `notebooks/05_modelagem/01_base_modelagem_diaria.ipynb`
- `notebooks/05_modelagem/02_catboost_lightgbm.ipynb`

Entradas:

- `Base_V2/features_filiais_diarias_V2.parquet`

Saidas:

- `Base_Modelagem/base_modelagem_diaria.parquet`
- `Base_Modelagem/features_modelagem.json`
- `Base_Modelagem/predicoes_catboost_lightgbm.parquet`
- `Base_Modelagem/metricas_catboost_lightgbm.parquet`
- `Base_Modelagem/importancias_catboost_lightgbm.parquet`

A clusterizacao saiu da pipeline oficial atual. A primeira rodada de modelagem segue com modelos globais CatBoost e LightGBM.

## Pendencias

- Definir a lista final de features da base de modelagem.
- Separar treino, validacao e teste por tempo.
- Decidir tratamento das metas zeradas.
- Avaliar se dados externos de CNES/municipios entram em uma versao futura.
