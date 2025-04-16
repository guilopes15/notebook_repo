n1 = int(input('Primeiro numero:'))
n2 = int(input('Segundo numero:'))
n3 = int(input('Terceiro numero:'))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor foi {menor}')
print(f'O maior valor foi {maior}')

# como o professor fez
# menor = n1
# if n2<n1 and n2<n3:
#   menor = n2
# if n3<n1 and n3<n2:
#   menor = n3
# ele ja atribuiu o menor sendo n1 dpois fez check no n2 e n3
