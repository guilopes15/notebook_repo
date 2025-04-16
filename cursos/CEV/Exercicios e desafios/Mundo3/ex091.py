from operator import itemgetter
from random import randint
from time import sleep

jogadores = {}

for c in range(1, 5):
    jogadores[f'Jogador{c}'] = randint(1, 6)

for jogador, dado in jogadores.items():
    print(f'{jogador} tirou {dado} no dado.')
    sleep(1)

rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-' * 30)
print('== Ranking dos jogadores ==')
for pos, items in enumerate(rank):
    print(f'{pos+1}º lugar: {items[0]} com {items[1]}.')
    sleep(1)

# todo anotar no caderno como ordenar dicionarios com itemgetter, e o parametro - key=itemgetter(posição)
