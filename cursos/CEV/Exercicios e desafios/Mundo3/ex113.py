def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except(ValueError, TypeError):
            print('Erro')
        except KeyboardInterrupt:
            print('Erro2')
        else:
            return inteiro


def leiafloat(msg):
    while True:
        try:
            real = float(input(msg))
        except:
            print('Erro')
        else:
            return real


num_inteiro = leiaint('Digite um numero inteiro:')
num_real = leiafloat('Digite um numero real:')
print(f'O numero inteiro foi {num_inteiro} e o real foi {num_real}')
