def metade(num=0):
    calc = num / 2
    return calc


def dobro(num=0):
    calc = num * 2
    return calc


def porcento(num=0, porcentagem=0):
    num += num * (porcentagem / 100)
    return num


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')


