from collections import ChainMap


a = {1: 'a', 2:'b', 3:'c'}
b = {2: 'x', 3: 'z', 4: 'w'}


# Liga varios dicts mas se conporta como um só, abedecendo a ordem 
# de precedencia dos parametros. É mais rápido do que criar um novo dicionário 
# e executar múltiplas chamadas de update().
c = ChainMap(a, b)


def chain(*iteraveis):
    for iteravel in iteraveis:
        yield from iteravel