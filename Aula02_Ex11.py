# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual 
# operação ele deseja realizar. O resultado da operação deve ser acompanhado
# de uma frase que diga se o número é:
# a. par ou ímpar
# b. positivo ou negativo
# c. inteiro ou decimal

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))
print('Qual operação desaja realizar?\n[A] - Adição\n[S] - Subtração\n[M] - Multiplicação\n[D] - Divisão')
escolha = input('Informe a operação: ')
if(escolha == 'A' or escolha == 'a'):
  adicao = numero1 + numero2
  resultado_Par_Impar = 'Par' if (adicao % 2 == 0) else 'Ímpar'
  resultado_Positivo_Negativo = 'Positivo' if (adicao >= 0) else 'Negativo'
  if(adicao // 1 == adicao):    
    print(f'O resultado da adição é {adicao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Inteiro')
  else:
    print(f'O resultado da adição é {adicao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Decimal')
elif(escolha == 'S' or escolha == 's'):
  subtracao = numero1 - numero2
  resultado_Par_Impar = 'Par' if (subtracao % 2 == 0) else 'Ímpar'
  resultado_Positivo_Negativo = 'Positivo' if (subtracao >= 0) else 'Negativo'
  if(subtracao // 1 == subtracao):    
    print(f'O resultado da subtração é {subtracao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Inteiro')
  else:
    print(f'O resultado da subtração é {subtracao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Decimal')
elif(escolha == 'M' or escolha == 'm'):
  multiplicacao = numero1 * numero2
  resultado_Par_Impar = 'Par' if (multiplicacao % 2 == 0) else 'Ímpar'
  resultado_Positivo_Negativo = 'Positivo' if (multiplicacao >= 0) else 'Negativo'
  if(multiplicacao // 1 == multiplicacao):    
    print(f'O resultado da multiplicação é {multiplicacao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Inteiro')
  else:
    print(f'O resultado da multiplicação é {multiplicacao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Decimal')
elif(escolha == 'D' or escolha == 'd'):
  divisao = numero1 / numero2
  resultado_Par_Impar = 'Par' if (divisao % 2 == 0) else 'Ímpar'
  resultado_Positivo_Negativo = 'Positivo' if (divisao >= 0) else 'Negativo'
  if(divisao // 1 == divisao):    
    print(f'O resultado da divisao é {divisao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Inteiro')
  else:
    print(f'O resultado da divisao é {divisao:.2f}, {resultado_Par_Impar}, {resultado_Positivo_Negativo} e Decimal')