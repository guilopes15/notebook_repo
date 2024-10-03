cont = 0
n = int(input('Digite um numero:'))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[35m', end='')
        cont += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print(f'\n\033[mO numero {n} foi divisivel {cont}')
if cont == 2:
    primo = 'É primo'
else:
    primo = 'Não é primo'
print(f'E por isso ele {primo}')
