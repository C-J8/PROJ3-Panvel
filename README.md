# PROJ3 Panvel

Projeto para organizar a preparacao de bases, EDA, clusterizacao de filiais e proxima etapa de modelagem de metas diarias da Panvel.

## Como navegar

- `docs/pipeline.md`: ordem oficial da pipeline e responsabilidades de cada etapa.
- `docs/inventario_colegas.md`: resumo do que veio dos colegas, o que foi movido e o que foi removido.
- `docs/faturamento.md`: regra adotada para faturamento bruto, liquido e devolucoes.
- `notebooks/01_pipeline_atual/`: notebooks oficiais ja ordenados.
- `notebooks/00_referencias/`: notebooks exploratorios dos colegas e historico de EDA.
- `reports/eda_bc/`: graficos e notas gerados pelo EDA dos colegas.
- `dados_externos/`: bases externas ainda nao integradas na modelagem.

## Bases

- `Base_Origi/`: dados brutos recebidos.
- `Base_V1/`: bases preparadas e escopo principal separado da `Base_exo`.
- `Base_V2/`: features para clusterizacao e analise diaria.
- `Base_exo/`: filiais jovens ou fora do escopo principal atual.
- `dados_externos/`: CNES e municipios, preservados para avaliacao futura.

## Ordem resumida

1. Preparar `Base_V1`.
2. Gerar features da `Base_V2`.
3. Clusterizar filiais.
4. Construir base de modelagem.
5. Treinar e avaliar modelos de previsao.
