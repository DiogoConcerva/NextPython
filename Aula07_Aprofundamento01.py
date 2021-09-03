# coding=utf8
# Escreva um programa que pergunte nomes de alunos de uma sala de aula. O número de alunos é
# desconhecido, por isso o programa deve perguntar até que seja digitada a palavra “fim”.
# Depois, o programa deve sortear um aluno para apresentar o trabalho primeiro.
# Exemplo:
# Digite um nome: Yann
#
# Digite um nome: Camilinha
#
# Digite um nome: Richardneydson
#
# Digite um nome: Claudiane
#
# Digite um nome: fim
#
# O primeiro aluno a apresentar será: Claudiane.

import random
alunos = []

def inserir_alunos():
    while True:
        nome = input('Informe o nome do aluno: ').lower()
        if nome == 'fim':
            break
        else:
            alunos.append(nome.capitalize())

def sorteio():
    escolha = random.randint(0, len(alunos))
    return alunos[escolha]

inserir_alunos()
print(f'O primeiro aluno a apresentar será: {sorteio()}.')
