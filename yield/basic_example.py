def funcao_geradora():
    yield 1
    yield 2
    yield 3


gerador = funcao_geradora()

next(gerador) # 1
next(gerador) # 2
next(gerador) # 3
next(gerador) # StopIteration


# Gera uma sequncia infinita de numeros impares sem ocupar memoria.
def impares():
    valor = 1
    while True:
        yield valor
        valor += 2