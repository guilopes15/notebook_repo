lista = (
    'APRENDER',
    'PROGRAMAR',
    'LINGUAGEM',
    'PYTHON',
    'CURSO',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMADOR',
    'FUTURO',
)
for palavra in lista:
    print(f'\nNa palavra {palavra} temos ', end='')
    for show_vogal in palavra:
        if show_vogal in 'AEIOU':
            print(f'{show_vogal}', end=' ')


# todo No primeiro for percorri todos os itens na lista,
# no segundo for percorri cada letra de cada item na lista
