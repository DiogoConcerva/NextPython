# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto
# quanto pagou ao INSS
# quanto pagou ao sindicato
# o salário líquido
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

ganho_hora = float(input('Informe quanto você ganha por hora R$ '))
horas_trabalhadas = float(input('Informe quantas horas trabalhadas no mês: '))
salarioBruto = ganho_hora * horas_trabalhadas
print(f'+ Salário Bruto: R$ {salarioBruto:.2f}')
print(f'- IR (11%): R$ {salarioBruto * 0.11:.2f}')
print(f'- INSS (8%): R$ {salarioBruto * 0.08:.2f}')
print(f'- Sindicato (5%): R$ {salarioBruto * 0.05:.2f}')
print(f'= Salário líquido: R$ {salarioBruto * 0.76:.2f}')
