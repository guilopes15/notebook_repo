lista = [
    1,
    2,
    3,
    4,
]
newlista = [lista[0]]
for acumulativo in lista[:3]:
    soma_acumulada = sum([newlista[acumulativo - 1], lista[acumulativo]])
    newlista.append(soma_acumulada)
print(newlista)
