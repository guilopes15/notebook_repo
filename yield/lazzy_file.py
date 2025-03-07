# Abre um arquivo sem ocupar memoria(lazzy/gerador).
path = 'yield/arquivo.txt'
arq = open(path)

# Chama linha por linha sem precisar ser o arquivo inteiro.
next(arq)
next(arq)
next(arq)

arq.close()

def file_generator():
    with open(path) as file:
        yield from file


