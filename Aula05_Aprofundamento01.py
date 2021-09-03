# Faça um programa para imprimir:
# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n

def imprimir(quantidade):
    for a in range(1, quantidade + 1):
        for b in range(a):
            print(a, end='\t')
        print('\n')

quantidade = int(input('Quantos números deseja imprimir? '))
imprimir(quantidade)
