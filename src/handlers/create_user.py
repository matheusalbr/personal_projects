from db.queries import get_insert_user_query
from db.db_connection import get_db_connection 
import json

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        connection = get_db_connection()
        cursor = connection.cursor()
        query = get_insert_user_query()
        cursor.execute(query, (data['nome'], data['email'], data['senha'], data['classe_usuario']))
        connection.commit()
        cursor.close()
        connection.close()
        response_body = {'message': 'User created successfully'}
        status_code = 201
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
