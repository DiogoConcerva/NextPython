# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo
# de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas

def somaImposto(taxaImposto, custo):
    print(f'O valor com imposto do produto é: R$ {((taxaImposto / 100) * custo) + custo:.2f}')

somaImposto(float(input('Informe a taxa de imposto em %: ')), float(input('Custo do produto sem imposto: ')))