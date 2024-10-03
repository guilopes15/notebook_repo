ptermo = int(input('Digite o primeiro termo:'))
razao = int(input('Razão da PA:'))
cont = 1
termo = ptermo
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('Pausa', end='')
    mais = int(input('\nQuantos termos a mais?'))
print(f'A PA foi finalizada com {total} termos mostrados.')
