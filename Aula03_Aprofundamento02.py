# Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25,
# imprime o nome da pessoa e a palavra “ACEITA”, caso contrario
# imprimir “NÃO ACEITA”

nome = input('Nome: ')
sexo = input('Sexo [M/F]: ').upper()
idade = int(input('Idade: '))
if(sexo == 'F' and idade < 25):
  print(nome, '\"ACEITA\"')
else:
  print('\"NÃO ACEITA\"')