# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit

c = float(input('Informe a temperatura em Celsius: '))
f = (c * (9 / 5)) + 32
print(f'{c}°C equivale a {f:.2f}°F')