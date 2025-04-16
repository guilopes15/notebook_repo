n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero:'))
    if n != 0:  # eliminando o 0(flag) da soma de pares e impares
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Vc Digitou {par} numeros pares e {impar} numeros impares')
