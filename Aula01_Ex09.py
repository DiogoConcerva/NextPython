# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius

f = float(input('Informe a temperatura em Fahrenheit: '))
c = 5 * ((f - 32) / 9)
print(f'{f}°F equivale a {c:.2f}°C')