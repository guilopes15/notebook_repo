lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(f'\nlanche ordenado {sorted(lanche)}')
print(f'Posição do Pudim: {lanche.index("Pudim")}')
