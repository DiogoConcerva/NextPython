# Faça um programa para converter uma letra maiuscula
# em letra minuscula. Use a tabela ASCII para resolver o problema

# ord corresponde ao número
# chr corresponde a letra

letra = input('Digite uma letra: ')
corresponde = ord(letra) + 32
print(chr(corresponde))