numeros = (
    int(input('Digite um numero:')),
    int(input('Digite outro numero:')),
    int(input('Digite mais um numero:')),
    int(input('Digite o ultimo numero:')),
)
print(f'O valor 9 apareceu {numeros.count(9) } vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1 }ª posição')
print(f'Os valores pares digitados foram', end='')
for par in numeros:
    if par % 2 == 0:
        print(f'{par:< 2}', end='')
