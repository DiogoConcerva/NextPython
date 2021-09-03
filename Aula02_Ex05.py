# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

data = input('Informe a data no formato dd/mm/aaaa: ').split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if(1 <= mes <= 12):
    if(1 <= dia <= 31):
        if(1 <= ano <= 9999):
            print('Data válida...')
        else:
            print('Ano inválido, tente novamente.')
    else:
        print('Dia inválido, tente novamente.')
else:
    print('Mês inválido, tente novamente.')