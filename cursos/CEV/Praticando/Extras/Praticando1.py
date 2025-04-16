# 1 litro de tinta pinta 3 m²
area = float(input('informe a area em m²:'))
metro_tinta = 1 / 3   # litros
lata_de_tinta = 18  # litros
preco_lata = 80
litros = area * metro_tinta
qlatas = 0
if area > 0:
    qlatas = 1
qlatas += litros // lata_de_tinta
if litros % lata_de_tinta == 0:
    qlatas -= 1
print(
    f'Vc precisa de {qlatas} latas que vai custar R${qlatas * preco_lata:.2f}.'
)

