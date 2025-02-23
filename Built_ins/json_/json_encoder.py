from json import JSONEncoder, dumps


# dumps() consegue converter tipos básicos do Python, 
# mas falha quando tentamos serializar objetos personalizados.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# O JSONEncoder é usado para personalizar a conversão de objetos Python
# para JSON. Isso é útil quando temos classes personalizadas que o 
# dumps() não sabe como serializar.
class PessoaEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pessoa):
            return {'nome': obj.nome , 'idade': obj.idade}
        return super().default(obj)
    

pessoa = Pessoa('Alice', 30)

json_string = dumps(pessoa, cls=PessoaEncoder)
    

# Tambem podemos usar o argumento default diretamente no dumps().
json_string = dumps(pessoa, default=lambda obj: obj.__dict__)
