lista = []
for valor in range(5):
    lista.append(int(input(f'Digite um valor para a posição {valor}:')))
print(f'Vc digitou os valores {lista}')
max_posicao = []
min_posicao = []
for pos, item in enumerate(lista):
    if item == max(lista):
        max_posicao.append(pos)
    elif item == min(lista):
        min_posicao.append(pos)
print(f'O maior valor digitado foi {max(lista)} nas posições {max_posicao}')
print(f'O menor valor digitado foi {min(lista)} nas posções {min_posicao}')
