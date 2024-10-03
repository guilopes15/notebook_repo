s = contmil = cont = menor = 0
menorpro = ''
while True:
    nomeP = str(input('Nome do produto:'))
    preco = float(input('Preço: R$'))
    s += preco
    cont += 1
    if cont == 1:
        menor = preco
        menorpro = nomeP
    else:
        if preco < menor:
            menor = preco
            menorpro = nomeP
    if preco > 1000:
        contmil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(
    f"""O total da compra foi R${s:.2f}
Temos {contmil} produtos custando mais de R$1000.00
O produto mais barato foi {menorpro} que custa RS{menor:.2f}"""
)

# todo definindo o menor preco e nome do mais barato sem usar funçao (min)
