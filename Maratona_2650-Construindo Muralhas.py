l = []
passaMuralha = []
entrada = input('Entrada: ').split()
quantidade, tamanho = int(entrada[0]), int(entrada[1])
for c in range(quantidade):
    inf = input('Informação: ').split()
    tita, nome, altura = inf[0].capitalize(), inf[1].capitalize(), int(inf[2])
    if altura > tamanho:
        passaMuralha.append(tita)
        passaMuralha.append(nome)
for c in passaMuralha:
    print(c)
