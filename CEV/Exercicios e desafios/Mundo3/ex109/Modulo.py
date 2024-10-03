def metade(num=0, formato=False):
    calc = num / 2
    return calc if not formato else moeda(calc)


def dobro(num=0, formato=False):
    calc = num * 2
    return calc if not formato else moeda(calc)


def aumento(num=0, porcen_aumento=0, formato=False):
    num += num * (porcen_aumento / 100)
    return num if not formato else moeda(num)


def desconto(num=0, porcen_desconto=0, formato=False):
    num -= num * (porcen_desconto / 100)
    return num if not formato else moeda(num)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num}'.replace('.', ',')









