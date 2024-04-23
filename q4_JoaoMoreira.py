import mysql.connector
DB_CONFIG = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'videogame_database'
}

# Expressões lambda para conexão e desconexão do banco de dados
connect_db = lambda config: mysql.connector.connect(**config)
disconnect_db = lambda conn: conn.close()

# Expressões lambda para geração de SQL de INNER JOIN e SELECT
generate_inner_join = lambda table1, table2, on_condition: f"INNER JOIN {table2} ON {on_condition}"
generate_select = lambda columns, table: f"SELECT {', '.join(columns)} FROM {table}"

# Função para criar e executar uma consulta SQL com INNER JOIN
execute_query_with_joins = lambda select_columns, joins, db_config: [
    result for result in [
        lambda conn: [
            conn.cursor().execute(
                f"{generate_select(select_columns, joins[0])} {' '.join([generate_inner_join(joins[i], joins[i + 1], condition) for i, condition in enumerate(joins[1:])])}"
            ),
            conn.cursor().fetchall() if "SELECT" in select_columns else None,
            disconnect_db(conn)
        ][1]
        for conn in [connect_db(db_config)]
    ][0]
]

# Consulta SQL de exemplo utilizando INNER JOIN entre GAMES, VIDEOGAMES e COMPANY
sql_query = lambda: execute_query_with_joins(
    ['GAMES.title', 'COMPANY.name AS company_name', 'VIDEOGAMES.name AS console_name', 'GAMES.release_date'],
    ["GAMES", "VIDEOGAMES", "COMPANY"],
    ["GAMES.id_console = VIDEOGAMES.id_console", "VIDEOGAMES.id_company = COMPANY.id_company"],
    DB_CONFIG
)

print(sql_query())
