from functools import total_ordering


# Preenche automaticamente métodos de comparação faltantes em classes, 
# baseando-se em __eq__ e um método de ordem.
@total_ordering
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, other):
        return self.idade == other.idade

    def __lt__(self, other):
        return self.idade < other.idade