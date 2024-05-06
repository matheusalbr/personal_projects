from ..db.queries import get_users_query
from ..db.db_connection import get_db_connection 
import json

def lambda_handler(event, context):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = get_users_query()
        cursor.execute(query)
        # Buscar todos os resultados
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        # Formatar a lista de usuários para JSON
        users_list = [{'nome': user[0], 'email': user[1], 'senha': user[2], 'classe_usuario': user[3]} for user in users]
        response_body = {'message': 'Users retrieved successfully', 'users': users_list}
        status_code = 200
    except Exception as e:
        # Fechando o cursor e a conexão em caso de erro
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
        response_body = {'error': str(e)}
        status_code = 500

    return {
        'statusCode': status_code,
        'body': json.dumps(response_body)
    }

