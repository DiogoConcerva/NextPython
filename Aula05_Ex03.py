# Crie um programa que possua uma lista de nomes. Peça que o usuário insira um nome que será
# buscado nesta lista. A busca deve ser implementada em uma função que retorna os valores lógicos
# verdadeiro ou falso.

def buscaNome(l, nome):
    for nomes in l:
        if(nomes == nome):
            return True
    return False

l = []
qtdNomes = int(input('Qunatos nomes deseja inserir? '))
nome = input('Qual nome deseja procurar? ')
for _ in range(qtdNomes):
    l.append(input(f'Digite um nome: '))
print(buscaNome(l, nome))
