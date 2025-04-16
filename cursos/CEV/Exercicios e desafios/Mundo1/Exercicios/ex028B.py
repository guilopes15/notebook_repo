import time
from random import randint

c = randint(0, 5)
print('-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar... ')
print('-' * 20)
n = int(input('Em que numero eu pensei?'))
print('Processando...')
time.sleep(2)
if c == n:
    print('Parabens! Vc venceu!')
else:
    print(f'Ganhei! Eu pensei no numero {c} e nao no numero {n}')
