# Dicionario EX:
pessoa = {'nome': 'Gui', 'idade': 24}

# Pratica da Aula:
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa'))
    estado['sigla'] = str(input('Sigla do estado'))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

