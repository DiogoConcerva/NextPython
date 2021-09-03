# Construa um dicionário para mapear o número do CEP dos seus colegas para o endereço da casa de
# cada um. Faça também um programa no qual o usuário insere o número do CEP e recebe como
# resposta o endereço.

entrada = ''
ceps = {}

while entrada != '3':
  entrada = input('1 - para inserir\n2 - para buscar\n3 - para sair\n')

  if entrada == '1':
    cep = input('Digite o CEP: ')
    endereco = input('Digite o endereço: ')
    ceps[cep] = endereco
  elif entrada == '2':
    cep = input('Digite o CEP que você está buscando: ')
    print(ceps[cep])
