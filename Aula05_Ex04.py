# Implemente um programa que possa receber do usuário a temperatura em graus Celsius ou Fahrenheit.
# Antes de receber a temperatura, pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit.
# Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit.
# Se a entrada for em Fahrenheit, o programa deverá retornar a temperatura em Celsius.

def transforma_celsius(temp):
    print(f'A temperatura equivalente a Celsius é {(temp - 32) * 5 / 9:.2f}ºC')

def transforma_fahrenheit(temp):
    print(f'A temperatura equivalente a Fahrenheit é {(temp * 9 / 5) + 32:.2f}ºF')

escolha = str(input('Deseja inserir a temperatura em Celsius (C) ou Fahrenheit (F)? Use C ou F: ')).upper()
if escolha == 'C':
    temp = float(input('Informe a temperatura em celsius: '))
    transforma_fahrenheit(temp)
elif escolha == 'F':
    temp = float(input('Informe a temperatura em fahrenheit: '))
    transforma_celsius(temp)
