# Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos
# existentes entre 1 e um número inteiro informado pelo usuário

numeroPrimo = int(input('Informe até que número deseja encontrar os números primos: '))
lista = list(range(1, numeroPrimo + 1))
p = []
total = 0
t = len(lista)
while t > 0:
    for c in range(len(lista), 0, -1):
        if(lista[-1] % c == 0):
            total += 1
    if(total == 2):
        p.append(lista[-1])
    lista.pop()
    total = 0
    t -= 1
del(lista)
p.sort()
print(p)