import colorize

n = 'guilherme'
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'peb': '\033[7;0',
}
print('Olá {}{}{}'.format('\033[4;34m', n, '\033[m'))
print('ola {}{}{}'.format(cores['azul'], n, cores['limpa']))
