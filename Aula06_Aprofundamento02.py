# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no
# seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa
# saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
# Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, com o nome
# dos usuários e seus repectivos consumos em Bytes chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um
# programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.       Uso do espaço em disco pelos usuários
#
#  Nr.  Usuário        Espaço utilizado     % do uso
#
#  1    alexandre       434,99 MB             16,85%
#  2    anderson       1187,99 MB             46,02%
#  3    antonio         117,73 MB              4,56%
#  4    carlos           87,03 MB              3,37%
#  5    cesar             0,94 MB              0,04%
#  6    rosemary        752,88 MB             29,16%
#
#  Espaço total ocupado: 2581,57 MB
#  Espaço médio ocupado: 430,26 MB

with open('usuarios.txt', 'w+') as arquivo:
    arquivo.write('alexandre      456123789')
    arquivo.write('\nanderson       1245698456')
    arquivo.write('\nantonio        123456456')
    arquivo.write('\ncarlos         91257581')
    arquivo.write('\ncesar          987458')
    arquivo.write('\nrosemary       789456125')

nomes = []
tamanhoByte = []
tamanhoMega = []
porcentagem = []

def espaco_disco(nome_arquivo):
    with open(nome_arquivo) as usuario_tamanho:
        for linha in usuario_tamanho:
            nomes.append(linha.split(linha[15])[0])
            tamanhoByte.append(int(linha.split()[1]))
        for c in tamanhoByte:
            tamanhoMega.append(c / pow(1024, 2))

def espaço_porcentagem(tamanhoMega):
    for c in tamanhoMega:
        porcentagem.append(c * 100 / 2581.5)

espaco_disco('usuarios.txt')
espaço_porcentagem(tamanhoMega)

with open('relatório.txt', 'w+') as relatorio:
    relatorio.write('''ACM Inc.       Uso do espaço em disco pelos usuários.
Nr.     Usuário         Espaço utilizado        % do uso''')
    for c in range(6):
        relatorio.write(f'\n{c + 1}\t\t{nomes[c]} {tamanhoMega[c]:.2f} MB\t\t\t\t{porcentagem[c]:.2f}%')

    relatorio.write(f'\n\nEspaço total ocupado: {sum(tamanhoMega):.2f} MB')
    relatorio.write(f'\nEspaço médio ocupado: {sum(tamanhoMega) / len(nomes):.2f} MB')
