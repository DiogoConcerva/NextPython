# Faça um programa para uma loja de tintas. O programa deverá pedir 
# o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da 
# tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida 
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a 
# quantidades de latas de tinta a serem compradas e o preço total. 
# Obs.: somente são vendidos um número inteiro de latas.

area = float(input('Informe a área em m² a ser pintada: '))
cobertura = 3 * 18
sobra = (area / cobertura) - (area // cobertura)
if area <= cobertura:
  print('Você precisa de uma lata de tinta. O valor é de R$ 80,00.')
elif (area > cobertura and sobra > 0):
  print(f'Você precisará de {(area // cobertura) + 1} latas e vai sobrar. O valor é de R$ {((area // cobertura) + 1) * 80}')
elif (area > cobertura and sobra == 0):
    print(f'Você precisará exatamente de {(area // cobertura)} latas. O valor é de R$ {(area // cobertura) * 80}')