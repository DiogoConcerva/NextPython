# Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e 
# fazer as consistências, informando ao usuário nas seguintes situações:
# a - Se o usuário informar o valor de A igual a zero, a equação não é do 
# segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado
# b - Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa
# c - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário
# d - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário

import math
a = float(input('Informe uma valor para a: '))
if a == 0:
  print('A equação não é do segundo grau. Programa encerrado.')
else:
  b = float(input('Informe uma valor para b: '))
  c = float(input('Informe uma valor para c: '))
  d = (b**2) - (4 * a * c) # Calculo de delta
  if(d < 0):
    print('A equação não possui raízes reais. Programa encerrado.')
  elif(d == 0):
    print(f'A equação possui apenas uma raíz real: {-b / (2 * a)}')
  else:
    raiz = math.sqrt(d)
    print(f'A equação possui duas raízes reais:\n{(-(b) - raiz) / 2 * a} e {(-(b) + raiz) / 2 * a}')
