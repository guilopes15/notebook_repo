def area(l, c):
    a = l * c
    print(f'A area de um terreno {l} x {c} é de {a}m².')


print('Controle de terrenos')
print('-' * 30)
largura = float(input('Largula (m):'))
comprimento = float(input('Comprimento (m):'))
area(largura, comprimento)
