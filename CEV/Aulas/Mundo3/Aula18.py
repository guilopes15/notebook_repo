galera = []
dado = []
maior = menor = 0
for c in range(3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 18:
        maior += 1
        print(f'{p[0]} é maior de idade')
    else:
        menor += 1
        print(f'{p[0]} é menor de idade')
print(f'Temos {maior} maiores e {menor} menores de idade.')
