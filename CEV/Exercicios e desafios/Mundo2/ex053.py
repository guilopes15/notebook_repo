frase = str(input('Digite uma frase')).replace(' ', '').lower()
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo ')
