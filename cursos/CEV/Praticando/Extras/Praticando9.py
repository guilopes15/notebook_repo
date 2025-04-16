def mediana(lista):
    sorted(lista)
    if len(lista) % 2 == 0:
        indice_meio1 = int((len(lista) / 2) - 1)
        indice_meio2 = int(len(lista) / 2)
        num_meio = lista[indice_meio1], lista[indice_meio2]
        return sum(num_meio) / 2
    else:
        return lista[len(lista)//2]


print(mediana([2, 2, 3, 2, 2, 3]))
