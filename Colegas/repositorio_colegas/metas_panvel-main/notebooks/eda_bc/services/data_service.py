def query_table(conn, query_string):
    cursor = conn.execute(query_string)
    
    try:
        rows = cursor.fetchall()
    except Exception as e:
        return [f"Erro: {str(e)}"]

    if not cursor.description:
        return ["Comando executado com sucesso."]

    if not rows:
        return ["(0 linhas)"]

    col_names = [desc[0] for desc in cursor.description]
    
    str_rows = [[str(item) if item is not None else "NULL" for item in row] for row in rows]
    str_cols = [str(col) for col in col_names]
    
    col_widths = [len(col) for col in str_cols]
    for row in str_rows:
        for i, item in enumerate(row):
            if len(item) > col_widths[i]:
                col_widths[i] = len(item)
                
    separator = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    header = "|" + "|".join(f" {col.ljust(w)} " for col, w in zip(str_cols, col_widths)) + "|"
    
    table = [separator, header, separator]
    for row in str_rows:
        table.append("|" + "|".join(f" {item.ljust(w)} " for item, w in zip(row, col_widths)) + "|")
    table.append(separator)
    
    return table

def show_tables(conn):
    tables = conn.execute("SHOW TABLES").fetchall()
    return [t[0] for t in tables]
    