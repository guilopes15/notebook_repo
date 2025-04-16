a = int(input('Digite um numero:'))
b = int(input('Digite um numero:'))

while a % b != 0:
    a, b = b, a % b
print(b)

