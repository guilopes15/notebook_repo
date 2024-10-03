v = int(input('Digite um valor para sacar:'))
ced = 50
totced = 0
while True:
    if v >= ced:
        v -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Vc sacou {totced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if v == 0:
            break

# todo no loop se v > ced tirar 50 e conta quantas vezes tirou 50 senao ced muda pra 20 ou 10 ou 1 e repete o loop.
