import duckdb
import os
import glob

def get_duckdb_connection():
    conn = duckdb.connect(database=':memory:')
    
    conn.execute("INSTALL httpfs;")
    conn.execute("LOAD httpfs;")
    
    datasets = {
        "devolucoes": "https://bkt-panvel-puc-projcd.s3.amazonaws.com/project-puc/devolucoes.parquet",
        "filiais": "https://bkt-panvel-puc-projcd.s3.amazonaws.com/project-puc/filiais.parquet",
        "metas": "https://bkt-panvel-puc-projcd.s3.amazonaws.com/project-puc/metas.parquet",
        "vendas": "https://bkt-panvel-puc-projcd.s3.amazonaws.com/project-puc/vendas.parquet"
    }

    for table_name, url in datasets.items():
        conn.execute(f"""
            CREATE OR REPLACE VIEW panvel__{table_name} AS 
            SELECT * FROM read_parquet('{url}');
        """)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    seeds_dir = os.path.join(base_dir, 'seeds')
    
    if os.path.exists(seeds_dir):
        for csv_path in glob.glob(os.path.join(seeds_dir, "*.csv")):
            table_name = os.path.splitext(os.path.basename(csv_path))[0]
            csv_path_safe = csv_path.replace('\\', '/')

            conn.execute(f"""
                CREATE OR REPLACE VIEW seed__{table_name} AS
                SELECT * FROM read_csv('{csv_path_safe}', sep=';', quote='"', header=True, auto_detect=True);
            """)

    return conn
