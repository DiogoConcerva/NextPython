# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos)

# 8 bits equivale a 1 byte
tamanho = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade do link em Mpps: '))
tempo = tamanho / (velocidade / 8)
print(f'O tempo aproximado de download do arquivo é de {tempo} segundos ou {tempo / 60} minutos')