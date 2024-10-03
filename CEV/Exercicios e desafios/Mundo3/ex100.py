from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(1, 10)
        print(n, end=' ')
        sleep(0.3)
        lista.append(n)
    print('Pronto!')


def somapar(lista):
    soma = 0
    for par in lista:
        if par % 2 == 0:
            soma += par
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []


sorteia(numeros)
somapar(numeros)
