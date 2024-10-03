def leiaint(msg):
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            break
        else:
            print('Erro! Digite um numero inteiro')
    return int(num)


n = leiaint('Digite um numero:')
print(f'Vc digitou o numero {n}')


#todo validando se o input retorna valor inteiro
