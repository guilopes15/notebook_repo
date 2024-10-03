s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {s}')

# cont é repetido entre os numeros impares divisiveis por 3, sendo assim da pra saber quantos numeros
# são pela quantidade de vezes que o cont apareceu.
