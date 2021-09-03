# Construa uma fun��o que receba uma string como par�metro e devolva outra string com os carateres
# embaralhados. Por exemplo: se fun��o receber a palavra python, pode retornar npthyo, ophtyn ou
# qualquer outra combina��o poss�vel, de forma aleat�ria. Padronize em sua fun��o que todos os
# caracteres ser�o devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados

import random

def embaralhar(palavra):
    embaralha = list(palavra)
    random.shuffle(embaralha)
    embaralha = ''.join(embaralha)
    print(embaralha.upper())

palavra = input('Digite uma palavra: ')
embaralhar(palavra)