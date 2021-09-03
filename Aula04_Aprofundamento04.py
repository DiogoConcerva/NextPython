# Faça um programa que calcule o mostre a média aritmética de N notas

l = []
while True:
  l.append(float(input('Informe a nota: ')))
  escolha = input('Deseja continuar [S/N]: ').upper()
  if escolha == 'N':
    break
print(f'Você informou {len(l)} notas e a média delas é {sum(l) / len(l)}')