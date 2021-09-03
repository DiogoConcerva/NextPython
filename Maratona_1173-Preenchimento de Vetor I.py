v = []
v.append(int(input('Informe o valor para primeira posição do vetor: ')))
if v[0] <= 50:
    for c in range(1, 10):
        v.append((v[c - 1] * 2))
for c in range(len(v)):
    print(f'N[{c}] = {v[c]}')
