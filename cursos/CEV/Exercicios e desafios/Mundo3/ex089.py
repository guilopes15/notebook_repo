lista = []
alunos = []
while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    alunos.append(nome)
    alunos.append(nota1)
    alunos.append(nota2)
    lista.append(alunos[:])
    alunos.clear()
    continuar = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        print('Resposta invalida')
        continuar = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 30)
print(f'No.{"nome":^15}{"media":^7}')
for pos, _ in enumerate(lista):
    media = (lista[pos][1] + lista[pos][2]) / 2
    print(f'{pos} {lista[pos][0]:^15} {media:^6}')
print('-' * 30)

while True:
    mostrar_notas = int(input('Mostrar notas de qual aluno?(999 interrompe)'))
    if mostrar_notas == 999:
        break
    if mostrar_notas <= len(lista) - 1:
        print(
            f'Notas de {lista[mostrar_notas][0]} são: {[lista[mostrar_notas][1],lista[mostrar_notas][2]]}'
        )

# todo o if com len(lista) -1 do ultimo while True,
# é para verificar se o numero do input mostrar_notas,
# corresponde a quantidade de alunos cadastrados na lista.
