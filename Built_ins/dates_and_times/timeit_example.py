import timeit


def minha_funcao():
    return sum(i**2 for i in range(1000))


# Cronometra o tempo de execução de uma funcao ou bloco de codigo.
tempo = timeit.timeit(lambda: minha_funcao(), number=1000)
print(f"Tempo decorrido: {tempo:.6f} segundos")