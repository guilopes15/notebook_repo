import urllib.request
import json


url = "https://test.com"

# Transforma o dict python em json
data = json.dumps({"nome": "Test", "sobrenome": "Conteúdo", "id": 1}).encode()
headers = {"Content-Type": "application/json"}

# Monta a requisição
req = urllib.request.Request(url, data=data, headers=headers, method="POST")

# Executa a requisição
response = urllib.request.urlopen(req)

print(response.status)
print(response.read().decode())
