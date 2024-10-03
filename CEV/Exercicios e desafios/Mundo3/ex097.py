def escreva(msg):
    separador = len(msg) + 4
    print('-' * separador)
    print(f'{msg:^{separador}}')
    print('-' * separador)


escreva('Gui')
escreva('Futuro')
escreva('Programador')
