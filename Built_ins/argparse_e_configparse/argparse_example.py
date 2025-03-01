from argparse import ArgumentParser


parser = ArgumentParser(
    prog='Calculadora',
    fromfile_prefix_chars='@'
)

# Choices funciona como um enum
parser.add_argument(
    'operacao', 
    type=str, 
    choices=['soma', 'subtracao', 'divisao', 'multiplicacao']
)

parser.add_argument('x', type=int)
parser.add_argument('y', type=int)

# A variavel verbose é um contador
parser.add_argument('-v', '--verbose', action='count', default=0)

# Agrupa todos os argumentos passados no cli
args = parser.parse_args()


def verbose(func):
    def inner(x, y):
        if args.verbose == 1:
            print(f'Operando com {x} e {y}')
        if args.verbose == 2:
            print(f'{func.__name__}({x} e {y})')
        if args.verbose >=10:
            print('Muito verboso, cancelando a operacao')
            return
        return func(x, y)
    return inner
    

@verbose
def soma(x, y):
    return x + y 


@verbose
def subtracao(x, y):
    return x - y 


@verbose
def divisao(x, y):
    return x / y 


@verbose
def multiplicacao(x, y):
    return x * y 


operacoes = {
    'soma': soma,
    'subtracao': subtracao,
    'divisao': divisao,
    'multiplicacao': multiplicacao,
}


print(operacoes[args.operacao](args.x, args.y))