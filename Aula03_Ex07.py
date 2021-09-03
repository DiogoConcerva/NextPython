# Entre com um nome e imprima o nome somente se a
# primeira letra do nome for “a” (maiuscula ou minuscula)

nome = input('Digite um nome: ')
if(nome[0] == 'a' or nome[0] == 'A'):
  print(nome)
else:
  print('Não inicia com A ou a')