# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

d = {1:'Domingo', 2:'Segunda-feira', 3:'Terça-feira', 4:'Quarta-feira', 5:'Quinta-feira', 6:'Sexta-feira', 7:'Sàbado'}
print('Informe um número:\n1-Domingo\n2-Segunda\n3-Terça\n4-Quarta\n5-Quinta\n6-Sexta\n7-Sábado')
num = int(input('Faça sua escolha: '))
print(d[num])
