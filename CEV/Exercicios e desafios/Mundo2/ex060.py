from math import factorial

fatorial = int(input('Digite um nume para calcular seu fatorial:'))
n = fatorial
calc = factorial(n)
print(f'Calculando {fatorial}! = ', end='')
while fatorial > 0:
    print(fatorial, end='')
    print('x' if fatorial > 1 else '=', end='')
    fatorial -= 1
print(calc, end='')

# O end='' faz com q os print fiquem na msma linha
