lista = (
    'aprender',
    'programar',
    'linguagem',
    'python',
    'curso',
    'gratis',
    'estudar',
    'praticar',
    'trabalhar',
    'mercado',
    'programador',
    'futuro',
)
vogais = 'aeiou'
for i in lista:
    print(f'\nNa palavra {i} temos ', end='')
    for vogal in i:
        if vogal in 'aeiou':
            print(vogal, end=' ')


# todo rever aula e refazer exercicio
