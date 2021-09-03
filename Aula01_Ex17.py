# Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a cobertura
# da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1 - comprar apenas latas de 18 litros
# 2 - comprar apenas galões de 3,6 litros
# 3 - misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias

area = float(input('Informe a área a ser pintada: '))
lataCobertura = 6 * 18
valorLata = 80.00
galaoCobertura = 6 * 3.6
valorGalao = 25.00
sobraLata = (area / lataCobertura) - (area // lataCobertura)
sobraGalao = (area / galaoCobertura) - (area // galaoCobertura)
areaAcrescimo = area * 1.1
if(sobraLata == 0):
  print(f'Você precisa levar extatamente {area // lataCobertura} lata(s) de tinta. Valor R$ {(area // lataCobertura) * valorLata}.')
else:
  print(f'Você precisa levar {area // lataCobertura + 1} latas de tintas e terá uma sobra. Valor R$ {(area // lataCobertura + 1) * 80}')
if(sobraGalao == 0):
  print(f'Você precisa levar extatamente {area // galaoCobertura} galão(ões) de tinta. Valor R$ {(area // galaoCobertura) * valorGalao}.')
else:
  print(f'Você precisa levar {area // galaoCobertura + 1} galão(ões) de tinta e terá uma sobra. Valor R$ {(area // galaoCobertura + 1) * valorGalao}.')
if(areaAcrescimo > 64.8) and (areaAcrescimo < 108):
  quantidadeLata = 1
  quantidadeGalao = 0
else:
  resto = areaAcrescimo % 108
  if resto == 0:
    quantidadeLata = areaAcrescimo // 108
  elif resto != 0 and resto > 64.8 and resto < 108:
    quantidadeLata = (areaAcrescimo // 108) + 1
    quantidadeGalao = 0
  else:
    quantidadeLata = areaAcrescimo // 108
    quantidadeGalao = resto if resto % 21.6 == 0 else (resto // 21.6) + 1
print(f'Você precisa levar {quantidadeLata} lata(s) e {quantidadeGalao} galão(ões) de tinta. Valor R$ {(quantidadeLata * valorLata) + (quantidadeGalao * valorGalao)}.')