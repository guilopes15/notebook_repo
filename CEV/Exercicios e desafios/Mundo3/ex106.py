from random import choice

cores = ('\033[m',
         '\033[0;0;40m',
         '\033[0;0;41m',
         '\033[0;0;42m',
         '\033[0;0;43m',
         '\033[0;0;44m',
         '\033[0;0;45m',
         '\033[7;0m'
         )


def decorador(msg):
    while True:
        ajuda = str(input(msg)).strip().lower()
        if ajuda != 'fim':
            print(choice(cores))
            help(ajuda)
            print(cores[0])
        else:
            break


print(f'''{choice(cores)}{"-"*30}
Sistema de ajuda Pyhelp
{"-"*30}
\033[m''')

decorador('Função ou biblioteca >')
