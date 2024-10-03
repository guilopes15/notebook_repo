continuar = ''
lista = []
while continuar != 'N':
    lista.append(int(input('Digite um valor:')))
    while True:
        continuar = str(input('Quer continuar?[S/N]')).strip().upper()[0]
        if continuar in 'S' or continuar in 'N':
            break
if 5 in lista:
    cinco = 'foi encontrado'
else:
    cinco = 'não foi encontrado'

lista.sort(reverse=True)

print('-=' * 30)
print(
    f"""Vc digitou {len(lista)} elementos
Os valores em ordem decrescente são {lista}
O valor 5 {cinco} na lista!"""
)
