def coroutime():
    print('Comecei')
    while True:
        value = yield # value so recebe um valor quando for enviado via send.
        yield from (x*10 for x in value)
        print('Acabou a sequencia')


coro = coroutime()

next(coro) # Comecei

# Uma forma de se comunicar com as coroutines
# Envia um dado para a variavel value dentro do gerador coroutine.
# O send tambem chama o next
coro.send([1, 2, 3]) # 10

next(coro) # 20
next(coro) # 30
next(coro) # Acabou a sequencia

# Quando acabar os valores da lista é necessario usando send para
# mandar outros valores por causa do while True.