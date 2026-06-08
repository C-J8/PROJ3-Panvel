# Projeto Panvel

**Integrantes**: Arthur Accorsi, Bruno Coliseli, Celso Junior, Gustavo Losch e Vinicius Pedroso.

## Descrição do Projeto

O projeto tem o objetivo prático de criar um sistema capaz de prever metas diárias de vendas para as farmácias Panvel do Paraná. Usando dados históricos de vendas e devoluções de 2024 e 2025, a ideia é aplicar machine learning e análise de séries temporais para calcular o valor de meta de cada loja no próximo mês, separando as projeções entre medicamentos e outros produtos.

Os conjuntos de dados utilizados abrangem informações detalhadas sobre faturamento, características físicas das lojas, localização geográfica, metas de vendas e registros de devoluções de produtos. A análise preliminar indica a importância de fatores como a metragem da área de venda e a localização das unidades no desempenho comercial.

## Estrutura do Repositório

O repositório está organizado para facilitar o acesso aos dados, scripts de processamento e documentação das análises:

- assets/: Contém recursos visuais relacionados à arquitetura do projeto e gráficos gerados durante as análises.
- notebooks/: Concentra as análises exploratórias e experimentos organizados por integrantes.
- src/: Módulos principais para aquisição e carregamento de dados (dataloader.py e download.py).

## Configuração do Ambiente

Para instalar as dependências necessárias utilize:

```bash
pip install -r requirements.txt
```

## Aquisição e Carregamento de Dados

O projeto utiliza a classe Dataloader (src/dataloader.py) para gerenciar o acesso aos arquivos em buckets S3. Os principais arquivos são: devolucoes.parquet, filiais.parquet, metas.parquet, vendas.parquet e filiais_dt_abertura.parquet.

Para baixar os dados localmente, execute o script `src/download.py`.

```bash
python src/download.py
```
