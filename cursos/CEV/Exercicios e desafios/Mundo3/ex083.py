expressao = input('Digite a expressão:')
verificar = []
for item in expressao:
    if item == '(':
        verificar.append('(')
    elif item == ')':
        if '(' in verificar:
            verificar.pop()
        else:
            verificar.append(')')
if len(verificar) == 0:
    print('Espressão valida')
else:
    print('Expressão invalida')
