a = input('Digite algo')
print(
    'O tipo primitivo desse valor é',
    type(a),
)
print('Só tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em maiusculas', a.isupper())
print('Está em minusculas?', a.islower())
print('Está capitalizada?', a.istitle())

# Alternativa com format (o check dentro do parenteses) ( a {} dentro do aspas)

print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?{}'.format(a.isspace()))
print('É um numero?{}'.format(a.isnumeric()))
print('É alfabetico?{}'.format(a.isalpha()))
print('É alfanumerico?{}'.format(a.isalnum()))
print('Está em maiusculas?{}'.format(a.isupper()))
print('Está em minusculas?{}'.format(a.islower()))
print('Está capitalizada?{}'.format(a.istitle()))


# Alternativa com new format
# a = input('Digite algo: ')
# print(f'O tipo primitivo desse valor é {type(a)}')
# print(f'Só tem espaços? {a.isspace()}')
# print(f'É um número? {a.isnumeric()}')
# print(f'É alfabético? {a.isalpha()}')
# print(f'É alfanumérico? {a.isalnum()}')
# print(f'Está em maiúsculas? {a.isupper()}')
# print(f'Está em minúsculas? {a.islower()}')
# print(f'Está capitalizado? {a.istitle()}')
