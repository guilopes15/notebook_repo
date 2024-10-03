cont = 1
ptermo = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
t = 0
termo = 10
while termo != 0:
    t += termo
    while cont <= t:
        calc = ptermo + (cont - 1) * razao
        cont += 1
        print(calc, end=' ')
        print('→ ' if cont != 0 else '', end='')
    print('Pausa', end='')
    termo = int(input('\nQuantos termos vc quer mostrar a mais?'))
print(f'Progressã finalizada com {t} termos mostrados.')

# a ordem/sequencia (de cima pra baixo) do T e do cont faz toda diferença no código
