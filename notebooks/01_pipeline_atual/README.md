# Pipeline Atual

Execute estes notebooks em ordem, a partir da raiz do projeto:

1. `01_preparacao_base_v1.ipynb`
2. `02_features_base_v2.ipynb`
3. `03_clusterizacao_filiais.ipynb`

Eles representam a pipeline oficial atual do projeto.

## Entradas e saidas

- `01_preparacao_base_v1.ipynb`: le `Base_Origi/` e salva `Base_V1/` e `Base_exo/`.
- `02_features_base_v2.ipynb`: le `Base_V1/` e salva features em `Base_V2/`.
- `03_clusterizacao_filiais.ipynb`: le `Base_V2/` e salva clusters/perfis em `Base_V2/`.

## Observacao

Os notebooks usam caminhos baseados em `Path.cwd()`. Abra o Jupyter a partir da raiz do repositorio para manter os caminhos corretos.
