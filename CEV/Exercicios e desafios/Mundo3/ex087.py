matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
terceira_coluna = []
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor para [{c},{i}]:'))
        if matriz[c][i] % 2 == 0:
            pares.append(matriz[c][i])
        if i == 2:
            terceira_coluna.append(matriz[c][i])
print('-' * 30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
print('-' * 30)
print(
    f"""A soma dos valores pares é {sum(pares)}
A soma dos valores da terceira coluna é {sum(terceira_coluna)}
O maior valor da sugunda linha é {max(matriz[1])}"""
)

# todo preenchendo e mostrando matriz
