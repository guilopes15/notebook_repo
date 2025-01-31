from itertools import product


sizes = ["P", "M", "G"]
colors = ["vermelho", "verde", "azul"]

# Evita for aninhado
for combination in product(sizes, colors):
    print(combination)