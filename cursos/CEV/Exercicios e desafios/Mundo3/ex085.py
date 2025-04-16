lista = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor:'))
    if valor % 2 == 0:
        lista[0].append(valor)
        lista[0].sort()
    else:
        lista[1].append(valor)
        lista[1].sort()
print('-' * 30)
print(
    f"""Os valores pares digitados foram {lista[0]}
Os valores impares digitados foram {lista[1]}"""
)
