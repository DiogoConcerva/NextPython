# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro

# b. Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

litros = float(input('Informe a quantidade de litros: '))
tipo = str(input('Informe\n[A] - Álcool ou [G] - Gasolina: '))
litroAlcool = 1.90
litroGasolina = 2.50
if((tipo == 'A' or tipo == 'a') and (litros <= 20)):
  print(f'O valor a ser pago é R$ {litros * (litroAlcool * 0.97):.2f}')
elif((tipo == 'A' or tipo == 'a') and (litros > 20)):
  print(f'O valor a ser pago é R$ {litros * (litroAlcool * 0.95):.2f}')
elif((tipo == 'G' or tipo == 'g') and (litros <= 20)):
  print(f'O valor a ser pago é R$ {litros * (litroGasolina * 0.96):.2f}')
elif((tipo == 'G' or tipo == 'g') and (litros > 20)):
  print(f'O valor a ser pago é R$ {litros * (litroGasolina * 0.94):.2f}')