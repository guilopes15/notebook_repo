d = float(input('Qual a distancia da viagem?'))
c1 = d * 0.5
c2 = d * 0.45
print(f'Vc está prestes a começar uma viagem de {d:.1f}Km')
if d > 200:
    print(f'E o preço da sua passagem será de R${c2:.2f}')
else:
    print(f'E o preço da sua passagem será de R${c1:.2f}')
