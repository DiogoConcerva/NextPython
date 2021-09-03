# Faça um programa que receba uma palavra e calcule
# quantas vogais (a, e, i, o, u) possui essa palavra.
# Entre com um caractere (vogal ou consoante) e substitua
# todas as vogais da palavra dada por esse caractere

palavra = input('Digite uma palavra: ')
print('a -',palavra.count('a'),'\ne -',palavra.count('e'),'\ni -',palavra.count('i'),'\no -',palavra.count('o'),'\nu -',palavra.count('u'))
substituicao = input('Entre com um caractere (vogal ou consoante) para substituir por todas as vogais: ')
print(palavra.replace('a', substituicao).replace('e', substituicao).replace('i', substituicao).replace('o', substituicao).replace('u', substituicao))