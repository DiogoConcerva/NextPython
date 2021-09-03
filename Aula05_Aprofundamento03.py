# Faça uma função que receba um valor inteiro e positivo e calcule o seu fatorial

def fatorial(fat):
    if fat == 0:
        return 1
    return fat * fatorial(fat - 1)

fat = int(input('Qual número deseja calcular seu fatorial? '))
print(fatorial(fat))