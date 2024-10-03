matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite o valor na posição[{c},{i}]'))

for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()

# todo fazendo um for dentro do outro para servir de contador,
# 1º FOR de 3 e o 2º FOR de 3, resultou no input 9 vezes.
