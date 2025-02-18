from collections import defaultdict


def valor_padrao():
    return "Valor não encontrado"


# Evita KeyError ao acessar chaves que ainda não foram definidas.
# Ao criar um defaultdict, você passa uma função que retorna o valor padrão. 
# Essa função será chamada automaticamente sempre que uma chave não 
# existente for acessada.
d = defaultdict(valor_padrao)

print(d['teste'])  # 'Valor não encontrado'
