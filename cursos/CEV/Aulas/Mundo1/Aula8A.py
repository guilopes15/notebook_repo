import math

n = int(input('Digite um numero:'))
r = math.sqrt(n)
print(
    f'A raiz de {n} é igual {r:.2f}, arredondado pra cima é {math.ceil(r)}, arredondado pra baixo é {math.floor(r)}'
)


# Usando de forma especifica

# from math import sqrt,ceil,floor
# n = int(input('Digite um numero:'))
# r = sqrt(n)
# print(f'A raiz de {n} é igual {r:.2f}, arredondado pra cima é {ceil(r)}, arredondado pra baixo é {floor(r)}')
