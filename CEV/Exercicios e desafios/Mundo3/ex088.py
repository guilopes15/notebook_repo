from random import randint, sample
from time import sleep

lista_numeros = []
lista_numeros_ordem = 0
print(
    f"""{'-'*30}
{'Joga na Mega sena':^30}
{'-'*30}"""
)
qjogos = int(input('Quantos jogos  vc quer que eu sorteie?'))
print(f"{'-'*5} Sorteando {qjogos} jogos {'-'*5}")
while len(lista_numeros) != 60:
    numeros = randint(1, 60)
    if numeros not in lista_numeros:
        lista_numeros.append(numeros)

for c in range(1, qjogos + 1):
    lista_numeros_ordem = sample(lista_numeros, 6)
    lista_numeros_ordem.sort()
    print(f'Jogo {c:>2}: {lista_numeros_ordem}')
    sleep(1)
