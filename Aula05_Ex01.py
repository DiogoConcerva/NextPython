# Crie um programa que receba um valor inteiro e avalie se
# ele é positivo ou negativo. Essa avaliação deve ocorrer
# dentro de uma função que retorna um valor booleano

def positivo_negativo(num):
  if num > 0:
    return True
  else:
    return False

num = positivo_negativo(float(input('Informe um número para análise: ')))
print(num)
