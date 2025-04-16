expressao = input('Digite a expressão:')
validacao = ''
for item in expressao:
    if expressao.count('(') == expressao.count(')'):
        validacao = 'Expressão valida'
    else:
        validacao = 'Expressão invalida'
print(validacao)
