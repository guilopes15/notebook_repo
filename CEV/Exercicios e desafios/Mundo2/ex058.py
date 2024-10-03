import random

n = random.randint(0, 10)
print(
    """Sou seu computador....
Acabei de pensar num numero entre 0 e 10.
Sera que vc consegue advinhar qual foi?"""
)
palpite = int(input('Qual seu palpite?'))
cont = 1
while n != palpite:
    if palpite < n:
        palpite = int(input('Mais... Tente mais uma vez.'))
    elif palpite > n:
        palpite = int(input('Menos ... Tente mais uma vez.'))
    cont += 1
if palpite == n:
    print(f'Vc acertou com {cont} tentativas. Parabéns!')
