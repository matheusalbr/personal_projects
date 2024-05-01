import psycopg2
from .db_config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

def get_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexão com o banco de dados estabelecida com sucesso.")
        return connection
    except psycopg2.Error as e:
        print(f"Falha ao conectar ao banco de dados: {e}")
        return None