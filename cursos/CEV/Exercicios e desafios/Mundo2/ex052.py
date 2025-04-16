cont = 0
n = int(input('Digite um numero:'))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO Numero {n} foi divisivel {cont} vezes')
if cont == 2:
    primo = 'É Primo'
else:
    primo = 'Não é primo'
print(f'E por isso ele {primo}')
