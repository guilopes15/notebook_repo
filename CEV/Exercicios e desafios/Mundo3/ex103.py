def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')


jogador = str(input('Nome do jogador:')).strip()
num_gols = str(input('Numero de gols:'))

if num_gols.isnumeric():
    num_gols = int(num_gols)
else:
    num_gols = 0

if jogador == '':
    ficha(gols=0)
else:
    ficha(jogador, num_gols)



#todo validando se o input é numerico e se esta vazio

