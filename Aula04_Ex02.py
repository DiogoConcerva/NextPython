# Crie uma lista de locais que você gostaria de conhecer no mundo,
# na ordem do local que você dá mais prioridade pra o local que você
# dá menos prioridade. Exiba a lista nas seguintes configurações:
# a) ordem original
# b) ordem alfabética
# c) ordem de prioridades inversa
# d) quantidade de itens

l = ['Taj Mahal', 'Grand Canyon', 'Parque Nacional de Yellowstone', 'Chapada dos Veadeiros', 'Coliseu', 'Parque do Jalapão']
print(f'Ordem original: {l}')
l.sort()
print(f'Ordem alfabética: {l}')
l.sort(reverse=True)
print(f'Ordem de prioridade inversa: {l}')
print(f'Quantidade de itens: {len(l)}')