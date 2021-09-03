# coding=utf8
# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
# contendo um relatório dos endereços IP válidos e inválidos. Será considerado um IP válido quando
# nenhuma de suas partes ultrapassar 255. O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256
# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
#  200.135.80.9
#  192.168.1.1
#  8.35.67.74
#  1.2.3.4
#  9.8.234.5
#
#  [Endereços inválidos:]
#  257.32.4.5
#  85.345.1.2
#  192.168.0.256

ipValidos = []
ipInvalidos = []

with open('ips.txt', 'w+') as ip:
    ip.write('200.135.80.9')
    ip.write('\n192.168.1.1')
    ip.write('\n8.35.67.74')
    ip.write('\n257.32.4.5')
    ip.write('\n85.345.1.2')
    ip.write('\n1.2.3.4')
    ip.write('\n9.8.234.5')
    ip.write('\n192.168.0.256')

def listaIp():
    with open('ips.txt') as ip:
        for linha in ip:
            if(int(linha.split('.')[0]) <= 255) and (int(linha.split('.')[1]) <= 255) and (int(linha.split('.')[2]) <= 255) and (int(linha.split('.')[3]) <= 255):
                ipValidos.append(linha)
            else:
                ipInvalidos.append(linha)

listaIp()

with open('relatórioIp.txt', 'w+') as relIp:
    relIp.write('[Endereços válidos:]' + '\n')
    for c in ipValidos:
        relIp.write(c)
    relIp.write('\n[Endereços inválidos:]' + '\n')
    for c in ipInvalidos:
        relIp.write(c)
