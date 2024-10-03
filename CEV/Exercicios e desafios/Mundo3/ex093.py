jogador = {}
jogador['nome'] = str(input('Nome do jogador:'))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))
gols = []
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {c}:')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-' * 30)
print(jogador)

print('-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for pos, gol in enumerate(jogador['gols']):
    print(f'=> Na partida {pos+1}, fez {gol} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
