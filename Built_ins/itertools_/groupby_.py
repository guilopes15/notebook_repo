from itertools import groupby

data = [
    ('apple', 'fruit'),
    ('carrot', 'vegetable'),
    ('pear', 'fruit'),
    ('broccoli', 'vegetable')
]

# Ordenado pelo index 1
data.sort(key=lambda x: x[1])

#Agrupa iteradores de mesma estrutura em categorias
gb = groupby(data, lambda x: x[1])

for key, g in gb:
    print(key, list(g))