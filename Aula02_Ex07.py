# Crie um programa para um circo, no qual dada a idade de uma pessoa,
# seja indicado o valor do ingresso segundo as regras:
# a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita
# b) a entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais
# c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais
# d) estudantes e professores pagam meia-entrada

idade = int(input('Informe a idade da pessoa: '))

if(idade < 4 or idade > 60):
  print('Entrada gratuita...')
elif(idade >= 4 and idade < 18):
  print('Entrada no valor de R$ 20,00 inteira ou R$ 10,00 caso seja estudante ou professor.')
else:
  print('Entrada no valor de R$ 30,00 ou R$ 15,00 caso seja estudante ou professor.')
