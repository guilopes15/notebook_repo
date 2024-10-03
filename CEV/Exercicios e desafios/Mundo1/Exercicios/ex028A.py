import random

n = int(input('Tente advinhar o numero que estou pensando:'))
escolha = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
if n == escolha:
    print(f'Vc acertou! Eu pensei no {escolha}')
else:
    print(f'Vc errou! Eu pensei no {escolha}')
