# Escrever um programa em Python que leia um vetor V1 de n posições e
# gere um vetor V2 de tamanho n que é o vetor V1 invertido

v1 = []
v2 = []
while True:
  v1.append(input('Entre com informações para o vetor V1: '))
  escolha = input('Deseja continuar [S/N]? ').upper()
  if(escolha == 'N'):
    break
v2 = v1[:]
v2.reverse()
print(f'Ordem de entrada do V1: {v1}')
print(f'Ordem de invertida no V2: {v2}')