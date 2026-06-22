# Preparação da Base V1

Este diretório contém a etapa de preparação das bases do projeto Panvel. O objetivo é transformar os arquivos brutos da `Base_Origi` em duas camadas tratadas:

- `Base_V1`: base principal, com filiais elegíveis para a próxima etapa de features;
- `Base_exo`: base preservada para filiais jovens, com menos de 24 meses de operação.

## Arquivo Principal

- `01_preparacao_base_v1.ipynb`

## Objetivos

A preparação executa:

- leitura dos arquivos originais em parquet;
- padronização de códigos de filial;
- separação de data e hora nas bases temporais;
- criação de `dia_semana`, `dia_semana_id` e `fim_semana_id`;
- criação de `vendas_diaria`;
- exclusão da filial `1704`, que aparece nas transações, mas não possui cadastro confiável;
- enriquecimento do cadastro com idade da filial;
- separação entre `Base_V1` e `Base_exo`;
- salvamento dos arquivos tratados.

## Entradas

Arquivos esperados em `Base_Origi/`:

- `project-puc_vendas.parquet`
- `project-puc_metas.parquet`
- `project-puc_filiais.parquet`
- `project-puc_filiais_dt_abertura.parquet`
- `project-puc_devolucoes.parquet`

## Saídas

Arquivos gerados em `Base_V1/`:

- `filiais_V1.parquet`
- `metas_V1.parquet`
- `vendas_V1.parquet`
- `vendas_diaria_V1.parquet`

Arquivos gerados em `Base_exo/`:

- `filiais_exo.parquet`
- `metas_exo.parquet`
- `vendas_exo.parquet`
- `vendas_diaria_exo.parquet`

## Regras Importantes

- A data de referência para idade da filial é `2025-12-31`.
- Filiais com menos de 24 meses são separadas para `Base_exo`.
- A filial `1704` é removida antes da separação por não possuir cadastro confiável.
- `dia_semana_id` usa `0=segunda-feira` até `6=domingo`.
- `fim_semana_id` usa `1` para sábado/domingo e `0` para dias úteis.
- Metas negativas da base original pertencem às filiais `1854` e `1857`, que vão para `Base_exo`; por isso, a `Base_V1` fica sem metas negativas.
- Metas zeradas são preservadas e devem ser investigadas antes da modelagem.

## Como Executar

O notebook detecta automaticamente a raiz do projeto procurando a pasta `Base_Origi/`. Ele pode ser executado a partir da raiz do projeto ou diretamente desta pasta.
