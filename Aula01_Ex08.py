# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Informe quanto você ganha por hora R$ '))
horas = float(input('Informe quantas horas trabalhada no mês: '))
print(f'O total do seu salário no mês é R$ {valor * horas:.2f}')