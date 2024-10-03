from time import sleep


def contagem(i, f, p):
    if p == 0:
        p = 1
    print(f'Comtando de {i} até {f} de {p} em {p}')
    if i > f:
        f -= 1
        p = -p

    elif i < f:
        f += 1

    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.3)
    print('Fim!')


contagem(1, 10, 1)
print('-' * 30)
contagem(10, 0, 2)
print('-' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
contagem(inicio, fim, passo)
