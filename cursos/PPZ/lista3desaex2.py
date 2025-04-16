preco_produto = int(input('Digite o preço do produto:'))
valor_pago = int(input('Valor pago:'))
troco = valor_pago - preco_produto
notas = [50, 20, 10, 5, 2, 1]
print('O troco é:')
for nota in notas:
    num_notas = troco // nota
    troco %= nota
    if num_notas != 0:
        print(f'{num_notas} notas de {nota}')
