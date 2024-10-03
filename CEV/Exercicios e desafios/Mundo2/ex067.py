while True:
    v = int(input('Quer ver a tabuada de qual valor?'))
    if v < 0:
        break
    for c in range(1, 11):
        print(f'{v} x {c:2} = {v * c}')
print('Programa encerrado. Volte sempre')
