nota1 = float(input('Informe a primeira nota:'))
nota2 = float(input('Informe a segunda nota:'))
media = (nota1 * nota2) / 2
status = ''
if media == 10:
    status = 'Aprovado com distinção'
elif media >= 7:
    status = 'Aprovado'
else:
    status = 'Reprovado'
print(f'O aluno está {status}')
