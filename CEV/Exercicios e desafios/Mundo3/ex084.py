pessoas = []
dados = []
continuar = ''
pesos = []
maior_peso = []
menor_peso = []

while continuar != 'N':
    nome = str(input('Nome:'))
    peso = float(input('Peso:'))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if continuar == 'N':
            break

for i in pessoas:
    pesos.append(i[1])
for itens in pessoas:
    if itens[1] == max(pesos):
        maior_peso.append(itens[0])
    if itens[1] == min(pesos):
        menor_peso.append(itens[0])

print(
    f"""Ao todo vc cadastrou {len(pessoas)} pessoas.
O maior peso foi {max(pesos)}Kg. Das pessoas {maior_peso}
O menor peso foi {min(pesos)}Kg. Das pessoas {menor_peso}"""
)
