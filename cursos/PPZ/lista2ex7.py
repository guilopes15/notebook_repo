# 1 litro de tinta pinta 3 m²
area = float(input('informe a area em m²:'))
metros_lata = 54
preco_lata = 80
if area % metros_lata == 0:
    latas = area / metros_lata
else:
    latas = int((area / metros_lata)) + 1
valor = int(latas) * preco_lata
print(f'Se necessario {latas} latas e vai custar {valor}')

