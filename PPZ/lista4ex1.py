from random import randint
lista = [randint(1, 100) for num in range(10)]
maior = menor = 0
for numero in lista:
    if numero > maior:
        maior = numero
    if menor == 0:
        menor = numero
    elif numero < menor:
        menor = numero
print(lista)
print(maior, menor)

