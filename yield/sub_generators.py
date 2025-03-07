# yield from ou 'produza de', substitui o for e aplica o protocolo iterator.
def impares(r):
    yield from (n for n in range(r) if n % 2 == 1)


def subcapitulos():
    yield 1.1
    yield 1.2
    yield 1.3

# yield from funciona como um sub gerador, que executa/chama outro gerador.
def capitulos():
    yield 1
    yield from subcapitulos()
    yield 2


cap = capitulos()

next(cap) # 1
next(cap) # 1.1
next(cap) # 1.2
next(cap) # 1.3
next(cap) # 2

# yield from chama outros geradores, mas tambem tranforma um
# objeto eager(ansioso), como uma lista, em lazzy(preguiçoso).
def my_gen():
    yield from range(42)
    yield from [1, 2, 3]