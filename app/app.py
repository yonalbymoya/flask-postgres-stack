from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola desde Flask, funciona de ostiaas"

@app.route('/db')
def db_test():
    try:
        conn = pyscopg2.connect(
                host=os.getenv("DB_HOST", "db"),
                database=os.getenv("POSTGRES_DB", "testdb"),
                user=os.getenv("POSTGRES_USER", "user"),
                password=os.getenv("POSTGRES_PASSWORD", "password")
                )
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        return f'Base de datos conectada: {version}'
    except Exception as e:
        return f'Error: {e}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

