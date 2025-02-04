# Multiple argument dispatching -> https://pypi.org/project/multimethod/
# Visitor pattern -> https://en.wikipedia.org/wiki/Visitor_pattern
# Polimorfismo/overload de funções
# Condições no dispatch com predicate dispatch -> https://github.com/pertsevds/predicate_dispatch
from functools import singledispatch


@singledispatch
def mostra_tipo(val):
    return 'N sei o tipo'


@mostra_tipo.register(int)
def _(val):
    print('É um inteiro')


@mostra_tipo.register
def _(val: list):
    print('É uma lista')


#Obs: singledispatch funciona apenas com tipos