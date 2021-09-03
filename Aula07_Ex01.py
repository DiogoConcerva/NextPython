# coding=utf8
# Usuario irá infomar o valor do raio, calcule a area da circuferencia utilizando funções e pi do modulo math.
# a. Faça o arredondamento apartir segunda casa decimal para cima
# b. Faça o arredondamento apartir terceira casa decimal para baixo

import math as m

def area(raio):
    a = m.pi * m.pow(raio, 2)
    print(f'Área sem arredondamento: {a}')
    print(f'Área com arredondamento de duas casas decimais para cima: {a:.2f}')
    print(f'Área com arredondamento de três casas decimais para cima: {m.floor((a * 1000)) / 1000}')

area(float(input('Informe o valor da raio: ')))