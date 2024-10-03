from random import randint
lista = [randint(1, 100) for c in range(20)]
impar = []
par = []

print(lista)
for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)


print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')
