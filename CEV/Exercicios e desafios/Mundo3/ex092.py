from datetime import date

cadastro = {}
cadastro['nome'] = str(input('Nome:'))
ano_nascimento = int(input('Ano de nascimento:'))
cadastro['idade'] = date.today().year - ano_nascimento
cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
if cadastro['ctps'] > 0:
    cadastro['contratacao'] = int(input('Ano de contratação:'))
    cadastro['salario'] = float(input('Salário: R$'))
    contribuicao = date.today().year - cadastro['contratacao']
    cadastro['aposentadoria'] = (cadastro['idade'] + 35) - contribuicao

print('-' * 30)
for k, v in cadastro.items():
    print(f'-{k} tem o valor {v}')


# formula da aposentadoria do prof
# cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] +35) - date.today().year)
