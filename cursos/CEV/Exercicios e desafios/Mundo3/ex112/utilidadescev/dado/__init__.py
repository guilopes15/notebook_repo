def leiadinheiro(num):
    while True:
        dinheiro = str(input(num)).strip().replace(',', '.')
        if dinheiro.isalpha() or dinheiro == '':
            print('Preço invalido')
        else:
            break
    return float(dinheiro)


