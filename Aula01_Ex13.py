# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input('Informe o sexo: [M/F] ')
h = float(input('Informe a altura: '))
if(sexo == 'M' or sexo == 'm'):
  print(f'Seu pesso ideal é {((72.7 * h) - 58):.2f} Kg')
else:
  print(f'Seu pesso ideal é {((62.1 * h) - 44.7):.2f} Kg')
