nome = str(input('Digite seu nome:')).strip()
juntando = nome.count(' ')
dividido = nome.split()
print('Analizando seu nome ... ')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - juntando} letras')
print(f'Seu primeiro nome tem {len(dividido[0])} letras')

# outra forma de contar o primeiro nome
# print('Seu primeiro n0me tem {} letras'.format(nome.find(' ')))
