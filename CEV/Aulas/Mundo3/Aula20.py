def soma(x, y):
    print(f'A soma de {x} e {y} é {x+y}')


def media(x=0, y=0):
    return (x + y) / 2


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')



soma(15, 23)
print(media(20))
contador(1, 2, 3, 3, 4, 8)


#todo Parametros posicionais na soma,
# nomeados na media,
# e empacotamento no contador.
