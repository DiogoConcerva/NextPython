# Construa uma pequena chave dicotômica para identificar uma determinada planta como
# membro de um dos principais grupos: Bryophyta, Pteridophyta, Gymnospermae ou Angiospermae.
# A identificação se dá com base na presença (1) ou ausência (0) de três caracteres:
# vascularização, sementes e flores. Utilize a tabela abaixo como referência.
# Grupo	        Vascularização	Sementes	Flores
# Bryophyta	            0	       0	       0
# Pteridophyta	        1	       0	       0
# Gymnospermae	        1	       1	       0
# Angiospermae	        1	       1	       1

# Estas variáveis armazenam a presença (1) ou ausência (0) de cada caractere
vasc = 1
sem = 0
flor = 0

# Seu código aqui
if(vasc == 0 and sem == 0 and flor == 0):
  print('Bryophyta')
elif(vasc == 1 and sem == 0 and flor == 0):
  print('Pteridophyta')
elif(vasc == 1 and sem == 1 and flor == 0):
  print('Gymnospermae')
elif(vasc == 1 and sem == 1 and flor == 1):
  print('Angiospermae')
