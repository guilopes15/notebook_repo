import math

co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hip = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hip:.2f}')

# Resolvendo sem o import
# (co**2 + ca**2)**(1/2)
