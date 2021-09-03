# Faça um programa que recebe um número de 1 a 10 do usuário
# e imprime a tabuada de multiplicação desse número

tabuada = int(input('Qual tabuada deseja estudar: '))
print('=-' * 30)
for numero in range(0, 11):
  print(tabuada, 'X', numero, '=', tabuada * numero)
print('=-' * 30)