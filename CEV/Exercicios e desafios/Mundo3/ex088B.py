from random import randint
from time import sleep

lista = []
cont = 0
print('   Jogando na Mega   ')
print('-' * 30)
jogos = []
qjogos = int(input('Quantos jogos quer sortear?'))
for _ in range(qjogos):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    cont = 0
    jogos.append(lista[:])
    lista.clear()
print(f'{"-"*5} Sorteando {qjogos} Jogos {"-"*5}')
for pos, itens in enumerate(jogos):
    print(f'Jogo{pos+1}: {itens}')
    sleep(1)
