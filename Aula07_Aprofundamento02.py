# coding=utf8
# Escreva um programa que receba o nome de uma sequência de times de futebol e exiba as partidas de um
# torneio com os times, de forma que:
# a) As partidas devem ser geradas de forma aleatória
# b) O número de times digitados deve ser par
# c) O programa deve pedir nomes até que seja digitado “fim” Exemplo
# Digite um time: Flamengo
# Digite um time: Vasco
# Digite um time: Fluminense
# Digite um time: Botafogo
# Digite um time: Bangu 2
# Digite um time: Barcelona
# Digite um time: fim
# Saída:
# Barcelona x Botafogo
# Fluminense x Vasco
# Bangu 2 x Flamengo

import random
times = []
equipes = 0

def inserir_time():
    while True:
        time = input('Digite o nome de um time: ').lower()
        if time == 'fim' and len(times) % 2 != 0:
            print('A quantidade de times deve ser par, informe um nome a mais um time.')
        elif time == 'fim' and len(times) % 2 == 0:
            break
        else:
            times.append(time.capitalize())

def sorteio():
    escolha = random.randint(0, len(times) - 1)
    time_sorteado = times[escolha]
    times.pop(escolha)
    return time_sorteado

inserir_time()
while len(times) != 0:
    print(f'{sorteio()} X {sorteio()}')
