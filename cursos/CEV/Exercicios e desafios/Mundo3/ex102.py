def factorial(numero, show=False):
    """
    -> Calcula o Factorial de um numero
    :param numero: O numero que vai ser calculado.
    :param show: Mostrar ou nao a conta (opcional).
    :return: Retorna do factorial de numero.
    """

    num = numero
    fatorar = 1
    while num > 0:
        fatorar *= num
        if show:
            print(num, end='')
            if num > 1:
                print('x', end='')
            else:
                print('=', end='')
        num -= 1
    return fatorar



print(factorial(5))
help(factorial)