# JSON (JavaScript Object Notation), é um formato leve de troca de dados 
# inspirado pela sintaxe de objeto JavaScript .
import json

# A serialização ou dumping é o processo de converter 
# objetos Python em strings JSON.
dados = {'nome': 'Alice', 'idade': 25}
json_string = json.dumps(dados)

# Parâmetros úteis
json_string = json.dumps(dados, indent=4, ensure_ascii=False)

# Escrevendo os dados JSON em um arquivo
with open('dados.json', 'w') as f:
    json.dump(dados, f)


# A desserialização ou loading converte strings JSON em objetos Python.
json_string = {'nome': 'Alice', 'idade': 25}
dados = json.loads(json_string)
print(dados["nome"]) # Alice


# Lê um arquivo JSON e converte para Python
with open('dados.json', 'r') as f:
    dados = json.load(f)


# Conversão de Tipos entre Python e JSON
print(json.dumps({"chave": None}))  # {"chave": null}


# Tratamento de erros
try:
    dados = json.loads('{"nome": "Alice", "idade": 25,,}') # Vírgulas extra

except json.JSONDecodeError as ex:
    print(f'Erro ao decodificar JSON: {ex}')

