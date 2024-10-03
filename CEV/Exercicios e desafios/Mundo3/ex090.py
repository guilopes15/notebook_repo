aluno = {}
aluno['nome'] = str(input('Nome:'))
aluno['media'] = float(input('Média:'))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'

elif aluno['media'] < 5:
    aluno['situação'] = 'Reprovado'

else:
    aluno['situação'] = 'Recuperação'

print('-' * 30)
for k, v in aluno.items():
    print(f'-{k} é igual a {v}')
