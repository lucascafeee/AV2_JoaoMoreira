from flask import Flask, request, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
import mysql.connector
from mysql.connector import Error

# a solução proposta foi construída com base na atividade 4, que envolveu o 
# desenvolvimento de um "Scaffold" para facilitar a escrita de consultas SQL complexas pros devs 
# interagindo com as tabelas GAMES, VIDEOGAMES, e COMPANY de um banco de dados MySQL.
app = Flask(__name__)
bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()

users = {
    "admin": bcrypt.generate_password_hash("supersecurepassword").decode('utf-8')
}

@auth.verify_password
def verify_password(username, password):
    return bcrypt.check_password_hash(users.get(username), password) if username in users else False

connect_db = lambda config: mysql.connector.connect(**config)
disconnect_db = lambda conn: conn.close() if conn.is_connected() else None

execute_query = lambda conn, query, params=(): (lambda cursor: [cursor.execute(query, params), cursor][1])(conn.cursor(buffered=True))

fetch_all = lambda cursor: cursor.fetchall() if cursor.with_rows else None

@app.route('/secure-query', methods=['POST'])
@auth.login_required
def secure_query():
    data = request.json
    query = data.get('query', '')
    params = data.get('params', ())

    if not query.strip().upper().startswith("SELECT"):
        return make_response("Apenas consultas SELECT são permitidas.", 403)

    try:
        conn = connect_db(DB_CONFIG)
        cursor = execute_query(conn, query, params)
        result = fetch_all(cursor) if cursor else None
        return jsonify(result), 200
    except Error as e:
        return make_response(f"Erro ao executar a consulta: {e}", 500)
    finally:
        if cursor: cursor.close()
        disconnect_db(conn)

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
