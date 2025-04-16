while True:
    num = int(input('Digite um numero inteiro positivo:'))
    if num > 0:
        break
cont = 0
for numero in range(1, num + 1):
    if num % numero == 0:
        cont += 1
if cont == 2:
    print('É primo')
else:
    print('Nao é primo')
