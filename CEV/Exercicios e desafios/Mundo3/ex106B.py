from time import sleep

cores = ('\033[m',
         '\033[0;0;40m',
         '\033[0;0;41m',
         '\033[0;0;42m',
         '\033[0;0;43m',
         '\033[0;0;44m',
         '\033[0;0;45m',
         '\033[7;0m'
         )


def ajuda(msg):
    titulo(f'Acessanddo o manual do comando {msg}', 4)
    print(cores[6], end='')
    sleep(0.5)
    help(msg)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cores[0], end='')
    sleep(0.5)


comando = ''
while True:
    titulo('Sistema de ajuda pyhelp', 2)
    comando = str(input('Funcao ou biblioteca >')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)

titulo('Ate logo')
