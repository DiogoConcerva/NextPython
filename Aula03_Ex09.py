# Faça um programa em que troque todas as ocorrencias
# de uma letra L1 pela letra L2 em uma string.
# A string e as letras L1 e L2 devem ser fornecidas pelo usuario

texto = input('Digite algo: ')
l1 = input('Informe a letra que deseja retirar: ')
l2 = input('Informe por qual letra deseja substituir: ')
print('O texto com as letras trocadas fica: ', texto.replace(l1, l2))