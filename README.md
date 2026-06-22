# PROJ3 Panvel

Projeto para organizar a pipeline de dados da Panvel, desde a análise exploratória até a preparação das bases, criação de features e modelagem de previsão.

## Visão Geral

A estrutura atual foi organizada para separar claramente:

- materiais de referência dos colegas;
- EDA consolidado;
- preparação da `Base_V1`;
- criação da `Base_V2`;
- modelagem diária de faturamento.

## Notebooks

- `notebooks/00_referencias/`: materiais exploratórios dos colegas e histórico preservado.
- `notebooks/01_eda/`: EDA consolidado oficial.
- `notebooks/02_preparacao/`: preparação da `Base_V1` e da `Base_exo`.
- `notebooks/03_features/`: criação da `Base_V2` e features consolidadas.
- `notebooks/05_modelagem/`: base de modelagem, baselines, CatBoost e LightGBM.

## Bases

- `Base_Origi/`: dados brutos recebidos.
- `Base_V1/`: bases tratadas, com filiais elegíveis para features.
- `Base_exo/`: filiais jovens ou fora do escopo principal atual.
- `Base_V2/`: features diárias e agregadas.
- `Base_Modelagem/`: base de modelagem, predições, métricas e importâncias dos modelos.
- `dados_externos/`: CNES e municípios, preservados para avaliação futura.

## Documentação

- `docs/pipeline.md`: ordem oficial da pipeline e responsabilidade de cada etapa.
- `docs/inventario_colegas.md`: resumo dos materiais recebidos dos colegas.
- `docs/faturamento.md`: decisão sobre faturamento bruto, líquido e devoluções.
- `docs/features_consolidacao.md`: features incorporadas a partir dos materiais do grupo.
- `docs/features_escolhidas.md`: features candidatas e pontos de cuidado para modelagem.
- `docs/modelagem_inicial.md`: primeira rodada de modelos CatBoost e LightGBM.
- `reports/data_quality.md`: checagem de qualidade e consistência das bases.
- `reports/eda_bc/`: gráficos e notas gerados pelo EDA dos colegas.

## Código e Recursos

- `src/`: scripts auxiliares, loaders e geradores de dados externos.
- `assets/`: imagens e recursos estáticos preservados.
- `.gitattributes`: configuração do Git LFS para arquivos grandes.
- `.gitignore`: arquivos e saídas ignoradas pelo Git.

## Ordem Recomendada

1. Revisar `notebooks/01_eda/`.
2. Executar `notebooks/02_preparacao/`.
3. Executar `notebooks/03_features/`.
4. Executar `notebooks/05_modelagem/01_base_modelagem_diaria.ipynb`.
5. Executar `notebooks/05_modelagem/02_catboost_lightgbm.ipynb`.
6. Avaliar e calibrar os modelos de previsão.

## Status Atual

- EDA: revisado e focado na etapa exploratória.
- Preparação: revisada, com `dia_semana_id` e `fim_semana_id` já criados na `Base_V1`.
- Features: revisada para reaproveitar o padrão de calendário da preparação.
- Clusterização: removida da pipeline oficial atual.
- Modelagem: primeira versão implementada com CatBoost e LightGBM.
