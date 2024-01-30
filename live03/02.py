
senha_correta = '123'
senha_digitada = ''

while senha_correta != senha_digitada:
    senha_digitada = input('Digite sua senha: ')
    if senha_correta != senha_digitada:
        print ('Senha incorreta, tente novamente!')

print ('Bem-vindo ao sistema!')