soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um numero:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Vc informou {cont} PARES e a SOMA foi {soma}')
