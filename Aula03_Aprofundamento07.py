# Faça um programa que leia uma palavra e some 1 no valor ASCII
# de cada caractere da palavra. Imprima a string resultante

# ord corresponde ao número
# chr corresponde a letra

palavra = input('Informe uma palavra: ')
for c in range(0, len(palavra)):
  alteracao = ord(palavra[c]) + 1
  print(chr(alteracao), end='')