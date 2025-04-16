def metade(num=0, formato=False):
    calc = num / 2
    return calc if not formato else moeda(calc)


def dobro(num=0, formato=False):
    calc = num * 2
    return calc if not formato else moeda(calc)


def aumento(num=0, porcentagem=0, formato=False):
    num += num * (porcentagem / 100)
    return num if not formato else moeda(num)


def desconto(num=0, porcentagem=0, formato=False):
    num -= num * (porcentagem / 100)
    return num if not formato else moeda(num)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0,porcen_aumento=0,porcen_desconto=0):
    print(f'''Preço analisado: \tR${num:.2f}
Dobro do preço: \t{dobro(num,True)}
Metade do preço: \t{metade(num,True)}
{porcen_aumento}% de aumento: \t{aumento(num,porcen_aumento,True)}
{porcen_desconto}% de redução: \t{desconto(num,porcen_desconto,True)}''')


#todo \t é uma tabulação, serve para organizar as proporçoes do texto
