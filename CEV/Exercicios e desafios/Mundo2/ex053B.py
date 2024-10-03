frase = str(input('Digite um frase:')).strip().upper().replace(' ', '')
frase_split = frase.split()
contrario = ''
for c in range(len(frase) - 1, -1, -1):
    contrario += frase[c]
print(f'O inverso de {frase} é {contrario}')
if frase == contrario:
    result = 'É um palindromo'
else:
    result = 'Não é um palindromo'
print(f'A frase digitada {result}')
