import sys
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
escolha = randint(0, 2)
print(
    """Suas opçoes:
[0] Pedra
[1] Papel
[2] Tesoura"""
)
player_esolha = int(input('Qual é a sua ecolha?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if escolha == 0:
    if player_esolha == 0:
        resultado = 'EMPATE'
    elif player_esolha == 1:
        resultado = 'VENCEU'
    elif player_esolha == 2:
        resultado = 'PERDEU'
    else:
        print('Opção invalida')
        sys.exit()
elif escolha == 1:
    if player_esolha == 0:
        resultado = 'PERDEU'
    elif player_esolha == 1:
        resultado = 'EMPATE'
    elif player_esolha == 2:
        resultado = 'VENCEU'
    else:
        print('Opção invalida')
        sys.exit()
elif escolha == 2:
    if player_esolha == 0:
        resultado = 'VENCEU'
    elif player_esolha == 1:
        resultado = 'PERDEU'
    elif player_esolha == 2:
        resultado = 'EMPATE'
    else:
        print('Opção invalida')
        sys.exit()
print(
    f"""O computador jogou {itens[escolha]}
O player jogou {itens[player_esolha]}
Você {resultado}"""
)
