texto = 'The Python Software Foundation and the global Python community ' \
        'welcome and encourage participation by everyone. Our community is based on mutual ' \
        'respect, tolerance, and encouragement, and we are working to help each other live up to' \
        ' these principles. We want our community to be more diverse: whoever you are, and' \
        ' whatever your background, we welcome you'.lower()
texto.replace(',',' ')
texto.replace('.',' ')
lista = texto.split()
lista2 = []
for palavra in lista:
        if palavra[0] in 'python' or palavra[-1] in 'python':
            lista2.append(palavra)

print(lista2)