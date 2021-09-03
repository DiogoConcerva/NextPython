# Escreva um programa que verifique se determinada entrada de
# usuário é um número. Considere válido números interios e reais,
# positivos e negativos, como: 10, -20, 103.0, -12.5

num = input('Digite uma valor: ')
try:
  float(num)
  print('Número válido')
except:
  print('Número inválido')