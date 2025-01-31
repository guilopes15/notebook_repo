from itertools import cycle
from time import sleep


semaforo = cycle(['Verde', 'Amarelo', 'Vermelho'])

for cor in semaforo:
    print(cor)
    sleep(2)