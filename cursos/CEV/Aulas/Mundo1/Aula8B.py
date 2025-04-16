import random

n = random.random()
n1 = random.randint(1, 10)
n2 = str(input('nome:'))
n3 = str(input('nome:'))
n4 = (n2, n3)
print(f'Numero random entre 0 e 1 = {n:.1f}')
print(f'Numero random entre 1 e 10 = {n1}')
print(random.choice(n4))
