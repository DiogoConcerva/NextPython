# Aumente a lista de heróis no arquivo herois.txt. Feito isso, crie um programa que leia esse arquivo e crie
# dois novos arquivos:
# 1 - Um arquivo apenas com heróis da Marvel;
# 2 - Outro apenas com heróis da DC;

dc = []
marvel = []

with open('herois.txt') as herois:
  for linha in herois:
    lista = linha.split(',')
    if 'DC' in lista[1]:
      dc.append(lista[0])
    else:
      marvel.append(lista[0])

def lista_arq(nome_arq, lista):
  with open(nome_arq, 'w') as arq:
    for linha in lista:
      arq.write(linha + '\n')

lista_arq('dc.txt', dc)
lista_arq('marvel.txt', marvel)
