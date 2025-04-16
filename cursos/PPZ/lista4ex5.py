texto = 'The Python Software Foundation and the global Python community ' \
        'welcome and encourage participation by everyone. Our community is ' \
        'based on mutual respect, tolerance, and encouragement, and we are working ' \
        'to help each other live up to these principles. We want our community ' \
        'to be more diverse: whoever you are, and whatever your background, we welcome you'.lower()
texto.replace(',', ' ')
texto.replace('.', ' ')
lista = texto.split()


def pitonica(text):
    for palavra in text:
        if palavra in 'python':
            return True
    return False


lista2 = [palavra for palavra in lista if pitonica(lista) and len(palavra)>4]
print(lista2)