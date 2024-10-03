from datetime import date

cont = 0
cont2 = 0
idade = 0
for c in range(1, 8):
    pessoa = int(input(f'Em que ano a {c}ª pessoa nasceu?:'))
    idade = date.today().year - pessoa
    if idade >= 21:
        cont += 1
    else:
        cont2 += 1
if cont != 0:
    print(f'Tivemos {cont} pessoas maiores de idade')
else:
    print('Nenhum maior de idade')
if cont2 != 0:
    print(f'Tivemos {cont2} pessoas menores de idade')
else:
    print('Nenhum menor de idade')
