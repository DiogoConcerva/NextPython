# Escreva um programa que implemente o jogo conhecido como pedra, papel, tesoura. Neste jogo,
# o usuário e o computador escolhem entre pedra, papel ou tesoura. Sabendo que pedra ganha de
# tesoura, papel ganha de pedra e tesoura ganha de papel, exiba na tela o ganhador:
# usuário ou computador. Para esta implementação, assuma que o número 0 representa pedra,
# 1 representa papel e 2 representa tesoura. O programa deve pedir para o usuário entrar com
# sua escolha, gerar aleatoriamente a escolha do computador, exibir a escolha e indicar o vencedor

import random
l = ['Pedra', 'Papel', 'Tesoura']

def escolha(usuario):
    computador = l[random.randint(0, 2)]
    if l[usuario] == computador:
        print(f'Empate, você escolheu {l[usuario]} e o computador também escolheu {computador}.')
    elif\
            (l[usuario] == l[0] and computador == l[2]) or \
                    (l[usuario] == l[1] and computador == l[0]) or\
                    (l[usuario] == l[2] and computador == l[1]):
        print(f'Você ganhou, sua escolha foi {l[usuario]} e o computador {computador}.')
    else:
        print(f'Você perdeu, sua escolha foi {l[usuario]} e o computador {computador}.')

print('''Escolha um das opções para jogar:
0 - Pedra
1 - Papel
2 - Tesoura''')
escolha(int(input('Digite sua escolha: ')))