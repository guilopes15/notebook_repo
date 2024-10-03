d = int(input('Quantos dias alugados?'))
km = float(input('Quantos km rodados?'))
r = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${r:.2f}')
