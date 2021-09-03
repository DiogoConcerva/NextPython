# Crie um programa que registra as notas de uma pessoa na escola (como o boletim) em um arquivo.
# Em seguida, leia todos os valores para imprimir o menor valor, o maior e a média.

with open('notas.txt', 'w') as notas:
  for _ in range(4):
    n = input('Insira a nota: ')
    notas.write(f'{n}\n')

with open('notas.txt') as notas:
  result = []
  for linha in notas:
    result.append(int(linha))
  print(f'A maior nota é {max(result)}')
  print(f'A menor nota é {min(result)}')
  print(f'A maior nota é {sum(result) / len(result)}')
