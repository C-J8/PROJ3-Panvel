# EDA - Projeto Panvel

Este diretorio contem a entrega consolidada de Analise Exploratoria de Dados (EDA) do projeto Panvel. O material foi organizado para funcionar como uma etapa independente da pipeline, podendo ser revisado diretamente no repositorio do projeto ou incorporado a uma entrega compartilhada do grupo.

## Arquivo Principal

- `01_eda_consolidado.ipynb`

O notebook consolida os principais achados exploratorios sobre vendas, metas, devolucoes, cadastro de filiais e cobertura temporal das bases.

## Como Executar

Execute o Jupyter a partir da raiz do projeto, mantendo a estrutura de pastas abaixo:

```text
Base_Origi/
Base_V1/
Base_V2/
Base_exo/
docs/
notebooks/
reports/
```

O notebook usa caminhos relativos ao diretorio raiz. Caso ele seja movido para outro repositorio, mantenha a mesma estrutura ou ajuste as variaveis de caminho nas primeiras celulas.

## Objetivos da EDA

A analise foi estruturada para responder:

1. Qual e a cobertura das bases em linhas, datas, filiais e colunas?
2. Existem divergencias entre cadastro de filiais e bases transacionais?
3. Quais filiais devem seguir para a base principal de modelagem?
4. Como tratar faturamento bruto, faturamento liquido e devolucoes?
5. Quais problemas precisam ser resolvidos antes da preparacao, features, clusterizacao e modelagem?

## Bases Avaliadas

Entradas principais:

- `Base_Origi/project-puc_vendas.parquet`
- `Base_Origi/project-puc_metas.parquet`
- `Base_Origi/project-puc_filiais.parquet`
- `Base_Origi/project-puc_filiais_dt_abertura.parquet`
- `Base_Origi/project-puc_devolucoes.parquet`

Bases derivadas consideradas na validacao:

- `Base_V1/`
- `Base_V2/`
- `Base_exo/`

## Principais Entregaveis

A EDA gera uma leitura consolidada sobre:

- consistencia de filiais entre cadastro, vendas, metas e devolucoes;
- cobertura temporal das bases;
- qualidade de metas, incluindo metas zeradas e negativas;
- diferencas entre faturamento bruto, devolucoes e faturamento liquido;
- separacao entre base principal (`Base_V1`) e filiais fora do escopo atual (`Base_exo`);
- pontos de atencao para a criacao de features e modelagem.

## Decisoes Registradas

- O faturamento bruto foi definido como alvo principal inicial.
- Devolucoes e faturamento liquido devem ser mantidos como diagnostico ou variaveis auxiliares.
- A filial `1704` foi excluida da base oficial por nao possuir cadastro confiavel.
- A `Base_V1` concentra 100 filiais elegiveis para as etapas seguintes.
- A `Base_exo` preserva 24 filiais jovens ou fora do escopo principal.
- Metas zeradas e datas ausentes devem ser tratadas antes da modelagem.

## Relacao Com a Pipeline

Esta EDA e a primeira etapa analitica da pipeline oficial. A sequencia recomendada apos sua revisao e:

1. preparar a `Base_V1`;
2. gerar a `Base_V2` com features consolidadas;
3. executar a clusterizacao de filiais;
4. construir a base final de modelagem;
5. treinar e avaliar modelos de previsao.

## Documentacao Complementar

Quando disponiveis no repositorio, os documentos abaixo complementam a EDA:

- `reports/data_quality.md`: checagem detalhada de qualidade das bases.
- `docs/faturamento.md`: decisao sobre faturamento bruto, liquido e devolucoes.
- `docs/features_consolidacao.md`: consolidacao das features incorporadas na `Base_V2`.
- `docs/pipeline.md`: ordem oficial das etapas do projeto.
