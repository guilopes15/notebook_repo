p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 0.05)
par = p + (p * 0.05)
numpar = 5
print(
    f'O produto custa R${d:.2f} a vista ou {numpar} parcelas de R${par/numpar:.2f}'
)
