# Faça um programa que leia 5 números e informe o maior número

numeros = 0
l = []
while numeros < 5:
  l.append(float(input(f'Informe o {numeros + 1}º número: ')))
  numeros += 1
print(f'O maior número é {max(l)}.')