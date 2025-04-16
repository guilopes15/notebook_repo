cont = 0
from random import randint

while True:
    v = int(input('Digite um valor:'))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou impar?[P/I]')).upper().strip()
    comp = randint(1, 10)
    s = v + comp
    if s % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
    print(
        f'Vo jogou {v} e o computador {comp}. Total de {v + comp} deu {resultado}'
    )
    if resultado[0] == escolha[0]:
        print(f'Voce Venceu! \nVamos jogar novamente...')
        cont += 1
    else:
        print('Vc perdeu!')
        break
print(f'Game Over! Vc venceu {cont} vezes')

# todo linha 5 e 6 é usada para repetir o input se nao tiver 'PI' na variavel escolha
