pa = 0
ptermo = int(input('Primeiro termo:'))
razao = int(input('Razao PA:'))
calc = 0
while pa != 10:
    pa += 1
    calc = ptermo + (pa - 1) * razao
    print(f'{calc} → ', end='')
    print('pausa' if pa == 10 else '', end='')
