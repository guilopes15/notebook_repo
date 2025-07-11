import time
import itertools
from threading import Thread, Event


def girar(msg, pronto):
    for char in itertools.cycle('|/-\\'):
        status = f'{char} {msg}'
        print(status, end='\r')
        if pronto.wait(0.5):
            break
    brancos = ' ' * len(status)
    print(f'\r{brancos}', end='\r')


def buscar():
    time.sleep(3)
    return 42


def main():
    pronto = Event()
    giradora = Thread(target=girar, args=['buscando a resposta ...', pronto])
    giradora.start()
    res = buscar()
    pronto.set()
    giradora.join()
    print('Resposta:', res)


main()
