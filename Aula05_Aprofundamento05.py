# Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”.
# Escreva um função que dado uma plavra verifique se ela é palindro

def verifica(palavra):
    l = list(palavra)
    resultado = 'É palíndromo' if l == l[::-1] else 'Não é palíndromo'
    print(resultado)

palavra = input('Digite uma palavra para verificarmos se ela é um palíndromo: ')
verifica(palavra)