# Você foi contratado para desenvolver um sistema de login para um 
# aplicativo da web. Sua primeira tarefa é criar uma tela de login 
# para autenticar os usuários.Para isso, você precisa escrever um 
# programa em Python que solicita ao usuário um nome de usuário 
# e uma senha. Em seguida, o programa verifica se o nome de usuário 
# e a senha correspondem a um par de login válido.
# Se o login for bem-sucedido, o programa deve exibir uma
# mensagem de boas-vindas com o nome de usuário. 
# Caso contrário, o programa deve exibir uma mensagem de 
# erro informando que o nome de usuário ou senha são inválidos.

usuario_cadastrado = 'leonid'
senha_cadastrada = '123'

usuario_digitado = input('Digite seu nome de usuário: ')
senha_digitada = input ('Digite sua senha: ')

if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
    print (f'Bem-vindo, {usuario_digitado}')
else:
    print (f'Usuário ou senha não cadastrados!')

