# Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações.

while True:
    nome = input('Informe o nome de usuário: ')
    senha = input('Informe a senha de usuário: ')
    if(senha == nome):
        print('Nome de usuário deve ser diferente da senha, tente novamente.')
    else:
        print('Cadastro realizado com sucesso.')
        break