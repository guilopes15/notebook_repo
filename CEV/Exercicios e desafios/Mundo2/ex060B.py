from math import factorial

f = int(input('Digite um numero para saber seu fatorial:'))
print(f'Calculando {f}! = ', end='')
for c in range(f, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
print(factorial(f), end='')

# O end='' faz com q os print fiquem na msma linha
