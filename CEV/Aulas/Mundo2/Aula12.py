import unidecode

n = str(input('Qual é o seu nome?')).strip().lower()
n = unidecode.unidecode(n)
if n == 'guilherme':
    print('Que nome bonito!')
elif n == 'pedro' or n == 'maria' or n == 'joao':
    print('Que nome popular vc tem!')
elif n in 'ana claudia jessica juliana':
    print('Belo nome feminino!')
else:
    print('Que nome comum vc tem !')
print(f'Tenha um bom dia, {n}!')

# unidecode remove acento
