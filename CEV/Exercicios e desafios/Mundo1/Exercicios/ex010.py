d = float(5.29)
i = float(0.039)
e = float(5.61)
n = float(input('Quanto de dinheiro vc tem na carteira? R$'))
print(f'Com R${n:.2F} vc pode comprar US${n/d:.2f}, ¥{n/i:.2f} e {n/e:.2f}€ ')
