# Faça um programa que crie uma pasta no diretorio atual do notebook e crie dentro dele um
# arquivo chamado, lista_de_chamada.txt, na qual devera ter 5 nomes informados pelo usuario

import os

def criar_pasta():
    if not os.path.exists('Aula07'):
        os.makedirs('Aula07')
    else:
        print('A pasta já existe.')

def criar_arquivo():
    if not os.path.exists('Aula07/Nomes.txt'):
        open('Aula07/Nomes.txt', 'w+')
    else:
        print('O arquivo já existe.')

def nomes():
    with open('Aula07/Nomes.txt', 'w+') as nome:
        for _ in range(5):
            nome.write(input('Informe um nome: ') + '\n')

criar_pasta()
criar_arquivo()
nomes()
