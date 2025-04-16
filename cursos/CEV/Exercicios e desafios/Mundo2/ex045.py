import sys
from random import choice
from time import sleep

from emoji import emojize

print('=' * 15, 'JOKENPÔ', '=' * 15)
print(
    """Sua opções:
[0] Pedra
[1] Papel
[2] tesoura"""
)
jogada = int(input('Qual é a sua jogada?'))
escolha = [
    emojize(':gem:', language='alias'),
    emojize(':scissors:'),
    emojize(':roll_of_paper:'),
]
comp_escolha = choice(escolha)
if jogada == 0:
    player_emoji = emojize(':gem:', language='alias')
elif jogada == 1:
    player_emoji = emojize(':scissors:')
elif jogada == 2:
    player_emoji = emojize(':roll_of_paper:')
else:
    print('Opção invalida')
    sys.exit()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print(
    '-=' * 20,
    '\n'
    f"""Computador jogou {comp_escolha}
Jogador Jogou {player_emoji}""",
)
if comp_escolha == player_emoji:
    resultado = 'EMPATE'
elif emojize(':scissors:') == comp_escolha and player_emoji == emojize(
    ':roll_of_paper:'
):
    resultado = 'PERDEU'
elif emojize(':roll_of_paper:') == comp_escolha and player_emoji == emojize(
    ':gem:', language='alias'
):
    resultado = 'PERDEU'
elif emojize(
    ':gem:', language='alias'
) == comp_escolha and player_emoji == emojize(':scissors:'):
    resultado = 'PERDEU'
else:
    resultado = 'VENCEU'
print('-=' * 20, f'\nJogador {resultado}')
