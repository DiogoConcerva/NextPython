l = []
def fibo(n):
    for c in range(n):
        if c == 0:
            l.append(0)
        elif c == 1:
            l.append(1)
        else:
            l.append(l[c - 1] + l[c - 2])


n = int(input('Informe um inteiro menor que 46: '))
if n < 46:
    fibo(n)
print(str(l).strip('[]').replace(',', ''))
