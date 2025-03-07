from contextlib import contextmanager
from datetime import datetime
from time import sleep


@contextmanager
def contador_de_tempo(var):
    print('Entrei no contexto')
    t0 = datetime.now()
    yield var
    delta = datetime.now() - t0
    print('Sai do contexto')
    print(f'Tempo total em segundos: {delta.seconds}')


with contador_de_tempo('variavel') as var:
    print('Dentro do contexto', var)
    sleep(3)

