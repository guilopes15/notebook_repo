lista = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1:'))
    nota2 = float(input('Nota2:'))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar?[S/N]'))
    if continuar in 'Nn':
        break
print('-' * 30)
print(f'{"No.":<4}{"Nome":<10}{"media":<8}')
for pos, item in enumerate(lista):
    print(f'{pos:<4}{lista[pos][0]:<10}{lista[pos][2]:<8}')
while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno?(999 interompe)'))
    if mostrar_notas == 999:
        break
    if mostrar_notas <= len(lista) - 1:
        print(
            f'Notas de {lista[mostrar_notas][0]} são {lista[mostrar_notas][1]}'
        )
