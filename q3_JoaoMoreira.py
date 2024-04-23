import mysql.connector
from mysql.connector import Error

db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'database': 'videogame_database'
}

def connect_db():
    """Estabelece a conexão com o banco de dados."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

def execute_query(query, params=None):
    """Executa uma consulta SQL com ou sem parâmetros."""
    try:
        conn = connect_db()
        if conn is not None:
            with conn.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                if query.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()
                else:
                    conn.commit()
            conn.close()
    except Error as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()

# Exemplos
execute_query("INSERT INTO COMPANY (name, country) VALUES (%s, %s)", ('Nintendo', 'Japan'))

companies = execute_query("SELECT * FROM COMPANY")
for company in companies:
    print(company)

execute_query("DELETE FROM COMPANY WHERE id_company = %s", (1,))

execute_query("INSERT INTO VIDEOGAMES (name, id_company, release_date) VALUES (%s, %s, %s)", ('Switch', 1, '2017-03-03'))

videogames = execute_query("SELECT * FROM VIDEOGAMES")
for videogame in videogames:
    print(videogame)
