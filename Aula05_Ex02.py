# Crie um programa que tenha uma função que receba uma lista de números inteiros e exiba todos
# os valores multiplicados por um valor inserido pelo usuário.

def multiplicacao(l, num_multiplicador):
    for num in l:
        print(num * num_multiplicador)

l = []
qtd_lista = int(input('Informe a quantidade de números que deseja inserir na lista: '))
num_multiplicador = int(input('Informe por qual números deseja multiplicar a lista: '))
for c in range(qtd_lista):
    l.append(int(input(f'Insira o {c + 1}º valor: ')))
multiplicacao(l, num_multiplicador)
