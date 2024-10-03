from random import randint

lista1 = [randint(1, 100) for _ in range(10)]
lista2 = [randint(1, 100) for _ in range(10)]
lista3 = []
for numero1, numero2 in zip(lista1, lista2):
    lista3.append(numero1)
    lista3.append(numero2)

print(lista1)
print(lista2)
print(lista3)
