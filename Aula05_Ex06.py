# Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos os
# seus valores em ordem invertida. Obs.: Sem usar invert ou o fatiador com passo -1

l = []

def ordena_contrario(l):
    for num in reversed(l):
        print(num)

def leitura_numeros(numeros):
    for c in range(numeros):
        l.append(int(input(f'Informe o {c + 1}º número: ')))
    ordena_contrario(l)
numeros = int(input('Quantos números deseja inserir na lista? '))
leitura_numeros(numeros)