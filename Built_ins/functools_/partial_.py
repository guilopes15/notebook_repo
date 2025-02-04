from functools import partial
# O partial funciona com o conceito de closure


def exponenciacao(x, y):
    return x ** y


# A ideia do partial é simplificar funções, 
# retornando uma nova função com o parametro fixado.
quadrado = partial(exponenciacao, 2)
cubo = partial(exponenciacao, y=3)

# Tambem é possiel fixar outras funçoes como argumento.
map_soma_1 = partial(map, lambda x: x + 1)
