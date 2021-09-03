entrada = input('Entre com a operação: ').replace('7', '0').split()
a, c, b = int(entrada[0]), entrada[1], int(entrada[2])
calculo = 0
if c == '+':
    calculo = a + b
else:
    calculo = a * b
calculo = int(str(calculo).replace('7', '0'))
print(calculo)