# Faça um programa que recebe do usuário 10 valores de números inteiros,
# armazena em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição

l = []
maior = posicao = 0
for n in range(0, 10):
  l.append(int(input(f'Informe o {n + 1}º número: ')))
  if n == 0:
    maior = l[n]
    posicao = n
  elif(l[n] > maior):
    maior = l[n]
    posicao = n
print(f'O maior valor é {maior} que está na posição {posicao} da lista.')