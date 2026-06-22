# Consolidacao de Features

Data da consolidacao: 2026-06-09.

Este documento registra o que foi incorporado ao notebook oficial `notebooks/03_features/01_features_base_v2.ipynb` a partir dos materiais do grupo.

## Resultado Atual

Arquivos regenerados:

| Base | Linhas | Colunas | Uso |
|---|---:|---:|---|
| `Base_V2/features_filiais_diarias_V2.parquet` | 73.082 | 110 | Base diaria principal para modelagem. |
| `Base_V2/features_filiais_agregadas_V2.parquet` | 100 | 49 | Perfil consolidado por filial. |

## O Que Entrou

| Origem | Ideia | Status | Onde entrou |
|---|---|---|---|
| BC | Primeiro dia util do mes | incorporado | `eh_primeiro_dia_util_mes` |
| BC | Quinto dia util do mes | incorporado | `eh_quinto_dia_util_mes` |
| BC | Feriados bancarios | incorporado | `eh_feriado_bancario`, `eh_dia_util`, `ordem_dia_util_mes`, `dias_uteis_no_mes` |
| BC | Ticket medio por filial | ja existia | `ticket_medio_bruto_dia_medio` e derivados |
| Gustavo | Fim de semana, mes, trimestre e fim de mes | ja existia ou expandido | calendario diario da V2, com `dia_semana_id` e `fim_semana_id` herdando o padrao da `Base_V1` |
| Gustavo | Lags de vendas | incorporado | `faturamento_bruto_lag_1d`, `7d`, `14d`, `28d` |
| Gustavo | Medias moveis | incorporado | `faturamento_bruto_media_movel_7d`, `28d` e variaveis auxiliares |
| Gustavo | Lags por categoria | incorporado em versao agregada | `faturamento_med_lag_7d`, `faturamento_n_med_lag_7d` |
| Celso | MED/N-MED, shares e perfil temporal | mantido | features diarias e agregadas |
| Celso/colegas | Cadastro de filiais | expandido | `localidade`, `uf`, `estacionamento`, `atendimento_24_horas`, `idade_filial_meses`, `idade_filial` |

## O Que Ficou Fora Por Enquanto

| Ideia | Motivo |
|---|---|
| Taxas de natalidade/mortalidade do BC | Os arquivos prontos dessas taxas nao estao disponiveis na arvore atual; existem apenas dados externos brutos/zips e scripts de geracao. |
| CNES/municipios | Preservados em `dados_externos/`, mas ainda precisam de chave confiavel de ligacao e validacao de cobertura. |
| Devolucoes/liquido como feature oficial | Mantidos como diagnostico por enquanto; a decisao atual e usar faturamento bruto como alvo principal. |
| Lags por categoria em granularidade transacional | A V2 oficial trabalha em granularidade diaria por filial; MED/N-MED foram incorporados em agregacao diaria. |

## Cuidados Para Modelagem

As novas features historicas foram calculadas com `shift(1)` antes das janelas moveis, evitando usar o proprio dia na media movel. Mesmo assim, a base diaria tambem contem colunas do dia observado, como `faturamento_bruto_dia`, `cupons_dia`, `quantidade_dia` e shares do proprio dia.

Na etapa de modelagem, sera necessario separar:

- alvo;
- features permitidas antes da previsao;
- features diagnosticas ou com vazamento de informacao;
- validacao temporal por filial.
