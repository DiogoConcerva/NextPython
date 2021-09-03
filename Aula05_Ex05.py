# Crie um programa que receba do usuário 5 números inteiros e os exiba na tela na ordem contrária a
# que foi inserido. A leitura dos números deve ser feita em uma função e a exibição dos valores em
# ordem contrária deve ocorrer em outra função.

l = []

def ordena_contrario(l):
    print(l[::-1])

def leitura_numeros():
    for c in range(5):
        l.append(int(input(f'Informe o {c + 1}º número: ')))
    ordena_contrario(l)
leitura_numeros()