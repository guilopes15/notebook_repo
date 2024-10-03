d = float(input('Qual a distancia da viagem?'))
p = d * 0.5 if d <= 200 else d * 0.45
print(f'Vc está prestes a começar uma viagem de {d:.1f}Km')
print(f'E o preço da sua passagem será de R${p:.2f}')
