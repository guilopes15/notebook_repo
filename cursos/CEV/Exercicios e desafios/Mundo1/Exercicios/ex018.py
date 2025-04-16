import math

an = float(input('Digite o angulo que voce deseja:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(
    f'O angulo de {an} tem o SENO de {sen:.2f}\nO angulo de {an} tem o COSSENO de {cos:.2f}'
)
print(f'O angulo de {an} tem a TANGENTE de {tan:.2f}')


# Convertendo para radians o parametro x - Python.org > docs > library > 9
# math.radians(x)
