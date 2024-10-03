jogador = {}
time = []
while True:
    jogador['nome'] = str(input('Nome do jogador:'))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))
    gols = []
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na partida {c}:')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    jogador.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('-' * 40)
print(f'{"cod"} {"nome":<15}{"gols":<15}{"total":<15}')
print('-' * 40)

for pos, i in enumerate(time):
    print(f'{pos:<4} ', end='')
    for v in i.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)

while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if dados == 999:
        break
    if dados <= len(time) - 1:
        print(f'--Levantamento do jogador {time[dados]["nome"]}')
        for pos, gol in enumerate(time[dados]['gols']):
            print(f' No jogo {pos+1} fez {gol} gols.')
    else:
        print(f'ERRO! Nao existe jogador com o codigo {dados}')


# todo validando informação do input dados
