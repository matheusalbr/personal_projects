def get_insert_user_query():
    return """
        INSERT INTO usuarios (nome, email, senha, classe_usuario, data_criacao, data_atualizacao)
        VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) RETURNING id;
    """
