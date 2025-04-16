from math import trunc

n = float(input('Digite um numero:'))
print(f'O valor digitado foi {n} e a sua porção inteira é {trunc(n)} ')

# Resolvendo sem import
print(f'O valor digitado foi {n} e a sua porção inteira é {int(n)}')
