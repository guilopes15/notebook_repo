f0 = 0
f1 = 1
f2 = 0
termo = int(input('Quantos termos vc quer mostrar?'))
cont = 0
print(f'{f0} → {f1} →', end='')
while cont < termo - 2:
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    cont += 1
    print(f'{f2} → ', end='')
print('Fim')
