# Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n

def imprimir(quantidade):
    for a in range(1, quantidade + 2):
        for b in range(1, a):
            print(b, end='   ')
        print('\n')

quantidade = int(input('Quantos números deseja imprimir? '))
imprimir(quantidade)
