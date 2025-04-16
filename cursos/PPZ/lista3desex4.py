num = int(input('Digite um numero:'))
for numero in range(2, num + 1):
    while num % numero == 0:
        print(numero)
        num /= numero

