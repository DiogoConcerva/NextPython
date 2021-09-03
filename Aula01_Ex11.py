# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1 - o produto do dobro do primeiro com metade do segundo.
# 2 - soma do triplo do primeiro com o terceiro.
# 3 - terceiro elevado ao cubo.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = float(input('Digite agora um número real: '))
print(f'O produto do dobro do primeiro com metade do segundo é {((2 * num1) * (num2 / 2))}')
print(f'A soma do triplo do primeiro com o terceiro é {((3 * num1) + (num3))}')
print(f'O terceiro elevado ao cubo é: {num3 ** 3}')