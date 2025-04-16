lista = list()
pos = 0
for v in range(5):
    n = int(input('Digite um valor:'))
    if v == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(lista)

# todo O 1º if é pra saber se é o 1º numero ou maior que o ultimo,
# o while e pra percorrer a lista e identificar aonde o numero vai ser inserido.
