dados = []
pessoa = {}
total = 0
mulheres = []

while True:
    pessoa['nome'] = str(input('Nome:')).strip()
    pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        print('Erro! Responda M ou f.')
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade:'))
    dados.append(dict(pessoa))
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['sexo'])
    total += pessoa['idade']
    pessoa.clear()

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        print('Erro! Responda S ou N.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
media = total / len(dados)

print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram {mulheres}')
print('Pessoas que estão acima da média')
for i in dados:
    if i['idade'] > media:
        print(f'nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')


# todo fazendo copia de dicionario: dict(variavel) ou variovel.copy()
