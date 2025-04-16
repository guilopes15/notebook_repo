nome = str(input('Digite seu nome completo:')).strip()
nome2 = nome.find(' ')
nome3 = nome.rfind(' ')
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0:nome2]}')
print(f'Seu ultimo nome é{nome[nome3:]}')

# Como o professor resolveu o ultimo nome
# nome4 = nome.split()
# print(f'Seu ultimo nome é {nome[len(nome4)-1]}')
