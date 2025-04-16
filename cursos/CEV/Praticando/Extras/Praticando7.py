lista = [1, 2, 3, 4]
newlist = []
while lista:
    for combinatoria in lista:
        newlist.append([lista[0], combinatoria + 1])
        if combinatoria == 4:
            lista.remove(lista[0])
            newlist.pop()
print(newlist)
