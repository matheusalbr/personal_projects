from handlers.create_user import lambda_handler

# Simulando um evento de entrada
event = {
    'nome': 'Teste Usuario',
    'email': 'teste3@exemplo.com',
    'senha': '12345678',
    'classe_usuario': 'ROLE_STAFF' 
}

# Simulando o contexto (não necessário neste teste)
context = {}

# Executando a função lambda_handler com os dados simulados
response = lambda_handler(event, context)

# Imprimindo a resposta para verificação
print(response)
