import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import os
import sys
import argparse

# Adiciona o diretório local ao path
sys.path.append(os.path.dirname(__file__))

from conn_models.duckdb_conn import get_duckdb_connection
from services import show_tables, query_table


DEBUG = False

def run_sql_query(query_name, conn=None):
    """Executa consultas SQL brutas da pasta queries/."""
    query_path = os.path.join(os.path.dirname(__file__), "queries", f"{query_name}.sql")

    if not os.path.exists(query_path):
        print(f"Erro: Arquivo {query_path} não encontrado.")
        return

    with open(query_path, "r", encoding="utf-8") as f:
        sql_content = f.read()

    if conn is None:
        conn = get_duckdb_connection()

    queries = [q.strip() for q in sql_content.split(';') if q.strip()]
    if not queries:
        print(f"Nenhuma query contida no arquivo {query_name}.")
        return

    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] Executando query")
        if DEBUG:
            print(f"\n{query}\n")
        
        resultados = query_table(conn, query)
        print(f"> Resultados:")
        for linha in resultados:
            print(f"  {linha}")

def run_query_df(conn, query_name):
    """Auxiliar para carregar query em DataFrame."""
    query_path = os.path.join(os.path.dirname(__file__), "queries", f"{query_name}.sql")
    with open(query_path, "r", encoding="utf-8") as f:
        sql_content = f.read()
    return conn.sql(sql_content).df()

def generate_categorical_eda():
    """Gera visualizações Seaborn focadas em análise por categoria (MED vs N-MED)."""
    print("Iniciando Categorical EDA...")
    conn = get_duckdb_connection()
    sns.set_theme(style="whitegrid")
    images_dir = os.path.join(os.path.dirname(__file__), "images")
    os.makedirs(images_dir, exist_ok=True)
    
    # Vendas
    print("  - Gerando imagem: Faturamento Mensal por Categoria...")
    vendas_df = run_query_df(conn, "eda__vendas__categorical")
    vendas_df['mes'] = pd.to_datetime(vendas_df['mes'])
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=vendas_df, x='mes', y='faturamento_total', hue='categoria_gerencial', marker='o')
    plt.title("Evolução do Faturamento Mensal por Categoria")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "vendas_categorical_trend.png"))
    plt.close()

    # Devoluções
    print("  - Gerando imagem: Devoluções Mensais por Categoria...")
    devol_df = run_query_df(conn, "eda__devolucoes__categorical")
    devol_df['mes'] = pd.to_datetime(devol_df['mes'])
    plt.figure(figsize=(12, 6))
    sns.barplot(data=devol_df, x='mes', y='valor_devolucao_total', hue='categoria_gerencial')
    plt.gca().set_xticklabels([d.strftime('%Y-%m') for d in devol_df['mes'].unique()], rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "devolucoes_categorical_bar.png"))
    plt.close()

    # Performance
    print("  - Gerando imagem: Atingimento de Meta Over Time...")
    perf_df = run_query_df(conn, "eda__performance__categorical")
    perf_df['mes'] = pd.to_datetime(perf_df['mes'])
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=perf_df, x='mes', y='percentual_atingimento', hue='categoria_gerencial', marker='s', linewidth=2.5)
    plt.axhline(100, ls='--', color='red', alpha=0.6, label='Meta (100%)')
    plt.ylim(0, max(perf_df['percentual_atingimento'].max() * 1.1, 110))
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "performance_achievement_trend.png"))
    plt.close()

def generate_deep_returns_eda():
    print("Iniciando Deep EDA de Devoluções...")
    conn = get_duckdb_connection()
    images_dir = os.path.join(os.path.dirname(__file__), "images")

    # Identificação de "Baixas em Massa" (Foco em Fechamentos de Trimestre)
    print("  - Gerando análises de picos com Centro de Massa...")

    # Carregamento e preparação dos dados
    mass_df = run_query_df(conn, "eda__devolucoes__mass_writeoffs")
    mass_df['data'] = pd.to_datetime(mass_df['data'])
    mass_df = mass_df.sort_values('data')

    # Configuração de estilo global do Seaborn para um visual mais limpo
    sns.set_theme(style="whitegrid", rc={"axes.spines.top": False, "axes.spines.right": False})

    metrics = [
        ('valor_total_dia', 'Valor Total no Dia (R$ x1000)', 'returns_quarterly_value.png'),
        ('ticket_medio_devolucao', 'Ticket Médio por Devolução (R$ x1000)', 'returns_quarterly_avg_ticket.png')
    ]

    years = mass_df['data'].dt.year.unique()

    for column, label, filename in metrics:
        fig, ax1 = plt.subplots(figsize=(15, 7))
        fig.patch.set_facecolor('white')  # Fundo branco limpo
        ax1.set_facecolor('white')

        ax2 = ax1.twinx()
        # Remover bordas do eixo secundário para visual limpo
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)

        # 1. Densidade de Massa Suavizada (Gaussian Smoothing)
        trend_series = mass_df.set_index('data')[column].resample('D').sum().fillna(0)
        # A janela com win_type='gaussian' cria as curvas orgânicas de sino (std define a largura do sino)
        rolling_trend = trend_series.rolling(window=30, win_type='gaussian', center=True, min_periods=1).mean(std=6)

        # Preenchimento com uma cor contrastante e sofisticada (Azul Ardósia)
        ax2.fill_between(
            rolling_trend.index,
            rolling_trend.values,
            color='#708090',
            alpha=0.25,
            label='Densidade de Volume (30d)',
            zorder=2
        )
        # Contorno da massa levemente mais escuro
        ax2.plot(rolling_trend.index, rolling_trend.values, color='#4a5560', lw=1.5, alpha=0.4, zorder=2)
        ax2.set_yticks([])

        # 2. Sombreamento dos Trimestres (Janelas de Fechamento)
        for year in years:
            for month in [3, 6, 9, 12]:
                first_day = pd.Timestamp(year=year, month=month, day=1)
                last_day = first_day + pd.offsets.MonthEnd(0)
                start_span = first_day - pd.Timedelta(days=10)
                end_span = last_day + pd.Timedelta(days=10)

                is_first = (year == years[0] and month == 3)
                ax1.axvspan(
                    start_span, end_span,
                    color='gray',
                    alpha=0.15,
                    label='Janela de Fechamento' if is_first else "",
                    zorder=1
                )

        # 3. Plot Principal (Scatter) - Com bordas brancas para destacar
        sns.scatterplot(
            data=mass_df,
            x='data',
            y=column,
            hue='categoria_gerencial',
            palette='Set1',
            alpha=0.85,
            s=180,
            edgecolor='white',
            linewidth=1.5,
            ax=ax1,
            zorder=4
        )

        # --- Ajustes Finais e Formatação ---
        ax1.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{x / 1000:,.1f}k'))

        # Unificar legendas e refinar caixa
        handles1, labels1 = ax1.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(
            handles1 + handles2, labels1 + labels2,
            loc='upper right',
            frameon=True,
            facecolor='white',
            edgecolor='#e0e0e0',
            framealpha=0.95,
            fontsize=10
        )

        ax1.set_title(f"Outliers e Centro de Massa: {label}", fontsize=15, pad=15, fontweight='bold', color='#333333')
        ax1.set_ylabel(label, fontsize=11, color='#555555', fontweight='bold')
        ax1.set_xlabel("Data", fontsize=11, color='#555555', fontweight='bold')

        ax1.tick_params(axis='x', rotation=45, colors='#555555')
        ax1.tick_params(axis='y', colors='#555555')

        # Grid eixo Y
        ax1.grid(axis='y', linestyle='--', color='#e0e0e0', alpha=0.7, zorder=0)
        ax1.grid(axis='x', visible=False)

        plt.tight_layout()
        plt.savefig(os.path.join(images_dir, filename), dpi=150, bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Panvel EDA Orchestrator")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    # Comando: run (SQL)
    run_parser = subparsers.add_parser("run", help="Executa uma consulta SQL da pasta queries/")
    run_parser.add_argument("query", help="Nome do arquivo .sql (sem extensão)")

    # Comando: plot-categorical
    subparsers.add_parser("plot-categorical", help="Gera gráficos EDA Categóricos (MED vs N-MED)")

    # Comando: plot-deep-returns
    subparsers.add_parser("plot-deep-returns", help="Gera gráficos avançados de Devoluções")

    # Comando: all
    subparsers.add_parser("all", help="Executa todas as suites de visualização")

    args = parser.parse_args()

    if args.command == "run":
        run_sql_query(args.query)
    elif args.command == "plot-categorical":
        generate_categorical_eda()
    elif args.command == "plot-deep-returns":
        generate_deep_returns_eda()
    elif args.command == "all":
        generate_categorical_eda()
        generate_deep_returns_eda()
    else:
        parser.print_help()
