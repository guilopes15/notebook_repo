from itertools import chain


letras = ['a', 'b', 'c']

n = [1, 2, 3]

for item in chain(letras, n): # Concatena iteraveis e transforma em geradores.
    print(item)

