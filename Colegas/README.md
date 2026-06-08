# Colegas

Esta pasta guarda o material recebido dos colegas e bases auxiliares para revisao antes de integrar na pipeline oficial do projeto.

## Estrutura

- `repositorio_colegas/metas_panvel-main/`: repositorio extraido do ZIP baixado do GitHub, com notebooks, scripts, queries SQL, imagens e documentacao dos colegas.
- `dados_panvel_duplicados/`: copias dos Parquets originais da Panvel. Estes arquivos foram comparados com `Base_Origi/` e sao iguais.
- `dados_panvel_duplicados/arquivos_invalidos/`: arquivos recebidos que nao carregam corretamente. Atualmente contem um Parquet vazio de vendas.
- `dados_externos/municipios/`: base geoespacial de municipios do Brasil.
- `dados_externos/cnes/`: CSVs compactados do CNES para 2024 e 2025.
- `zips_originais/`: arquivos compactados originais preservados como recebidos.

## Pontos importantes

- O ZIP `metas_panvel-main.zip` foi extraido para `repositorio_colegas/metas_panvel-main/`.
- Os Parquets em `dados_panvel_duplicados/` nao parecem trazer informacao nova em relacao a `Base_Origi/`.
- O material mais aproveitavel para a proxima etapa parece estar em `repositorio_colegas/metas_panvel-main/notebooks/eda_bc/`, especialmente as queries DuckDB e scripts de seeds.
