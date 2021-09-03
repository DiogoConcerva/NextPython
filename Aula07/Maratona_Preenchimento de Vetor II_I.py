entrada = int(input('Entrada: '))

if 2 <= entrada <= 50:
    n = list(range(0, entrada))
    valor = n * 1000
    for c in range(1000):
        print(f'N[{c}] = {valor[c]}')
