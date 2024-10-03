def teste(b):
    """
    -> Escopo de variavel

    :param b: recebe um parametro global
    :return: retorna os valores locais

    """
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')


#todo a variavel {a} tem dois valores diferentes, o global e o local(dentro da função).
