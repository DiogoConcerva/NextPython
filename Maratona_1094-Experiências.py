n = int(input('Quantidade de testes: '))
q = []
co = 0
r = 0
s = 0
total = 0
for c in range(0, n):
    q.append(input('Quantidade de cobaias: ').upper().split())
    if 1 <= int(q[c][0]) <= 15:
        total += int(q[c][0])
        if q[c][1] == 'C':
            co += int(q[c][0])
        elif q[c][1] == 'R':
            r += int(q[c][0])
        elif q[c][1] == 'S':
            s += int(q[c][0])
print(f'Total: {total} cobaias')
print(f'Total de coelhos: {co}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {co * 100 / total:.2f} %')
print(f'Percentual de ratos: {r * 100 / total:.2f} %')
print(f'Percentual de sapos: {s * 100 / total:.2f} %')