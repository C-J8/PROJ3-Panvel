# Panvel EDA - Business Context (BC)

Este diretório contém o orquestrador e as consultas para a realização da Análise Exploratória de Dados (EDA) dos datasets da Panvel.

## Estrutura de Diretórios

- `queries/`: Contém os arquivos SQL (.sql).
- `images/`: Gráficos gerados automaticamente em formato PNG.
- `notes/`: Relatórios em Markdown consolidando as visualizações e interpretações.
- `conn_models/`: Utilitários de conexão com o banco de dados.

## Como Executar

### 1. Criar e ativar o Ambiente Virtual (Certifique-se que esta no diretorio eda_bc)
```bash
cd notebooks/eda_bc/

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

### 2. O Orquestrador Unificado (`main.py`)
Utilizamos o `main.py` como ponto de entrada único via CLI:

#### Rodar uma Query SQL Específica
```bash
python main.py run <nome_da_query>
# Exemplo: python main.py eda__vendas__categorical
```

#### Gerar Gráficos Categóricos (Seaborn)
```bash
python main.py plot-categorical
```

#### Gerar Deep EDA de Devoluções
```bash
python main.py plot-deep-returns
```

#### Gerar Todas as Visualizações de uma vez
```bash
python main.py all
```

## Dependências Principais
- `duckdb`: Processamento SQL.
- `pandas`: Manipulação de dados.
- `seaborn` & `matplotlib`: Visualização estatística.

---

## Feature Engineering

As features são consolidadas pela query `eda__features__engineering.sql` e enriquecem o dataset de vendas diário com contexto temporal, demográfico e comercial.

### Features

| Feature | Tipo | Descrição |
|---|---|---|
| `fl_primeiro_dia_util` | `INT` (0/1) | Flag indicando se a data é o 1º dia útil do mês |
| `fl_quinto_dia_util` | `INT` (0/1) | Flag indicando se a data é o 5º dia útil do mês |
| `taxa_mortalidade_cidade` | `FLOAT` | Taxa de mortalidade do município (por 1000 habitantes) |
| `taxa_natalidade_cidade` | `FLOAT` | Taxa de natalidade do município (por 1000 habitantes) |
| `ticket_medio_filial` | `FLOAT` | Ticket médio histórico da filial (faturamento / num. de documentos únicos) |

---

### Origem e Tratamento dos Dados

#### Flags de Dia Útil (`fl_primeiro_dia_util`, `fl_quinto_dia_util`)
Calculadas inteiramente em SQL por `ROW_NUMBER() OVER (PARTITION BY mes ORDER BY data)`, com exclusão de:
- **Finais de semana**: filtro `dayofweek(data) NOT IN (0, 6)` (0=Dom, 6=Sáb).
- **Feriados nacionais bancários** (fixos e móveis): via join com a seed `seed__feriados`, que inclui Carnaval (Seg/Ter), Sexta-feira Santa, Corpus Christi e fecho bancário de ano (31/Dez ou último dia útil antes).

#### Taxas Demográficas (`taxa_mortalidade_cidade`, `taxa_natalidade_cidade`)
- **Fonte**: APIs públicas do IBGE — [Pesquisa 39 (Mortalidade Infantil)](https://servicodados.ibge.gov.br) e [SIDRA Tabela 6579 (População Estimada)](https://apisidra.ibge.gov.br).
- **Granularidade**: por município e por **ano** — o join na query usa `YEAR(data_venda) = ano` para aplicar os indicadores do ano correto a cada transação.
- **Cobertura de anos**: 2020–2025. Os dados de nascimentos/óbitos estão disponíveis no IBGE até 2023; para 2024 e 2025 os valores são propagados a partir de 2023 (carry-forward), cruzados com a população estimada de cada ano.
- **Fórmula da Taxa de Natalidade**: `(Nascidos Vivos / População Estimada) × 1000`.

#### Ticket Médio por Filial (`ticket_medio_filial`)
Calculado diretamente em SQL sobre `panvel__vendas`:
```sql
SUM(faturamento) / COUNT(DISTINCT codigo_documento_saida)
```
Representa o valor médio por cupom/documento de saída único, calculado sobre todo o histórico disponível.

---

### Seeds (Dados Externos)

Os dados externos são armazenados em `seeds/` e carregados automaticamente pelo DuckDB como views com prefixo `seed__`.

| Arquivo | View DuckDB | Descrição |
|---|---|---|
| `seeds/feriados.csv` | `seed__feriados` | Feriados nacionais bancários de 2023 a 2026 |
| `seeds/dados_cidades.csv` | `seed__dados_cidades` | Taxas demográficas anuais (2020–2025) das 28 cidades |

### Como Reconstruir as Seeds

Caso esteja rodando a primeira vez ou precise atualizar os dados externos (ex.: novo ano disponível no IBGE), execute os scripts em `scripts/` a partir da raiz do projeto:

```bash
# Recalcula os feriados para novos anos
python eda_bc/scripts/generate_holidays_seed.py

# Refetch dos dados demográficos do IBGE via API
python scripts/generate_demographics_seed.py
```

Os scripts escrevem diretamente em `seeds/`, sobrescrevendo os arquivos anteriores.

### Como Rodar a Query de Feature Engineering

```bash
# A partir da raiz do eda_bc, com o VENV iniciado e configurado
python main.py run eda__features__engineering
```
