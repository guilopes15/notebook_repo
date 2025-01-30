class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        self._nome_completo = f'{self.nome} {self.sobrenome}'
        

    @property
    def nome_completo(self):
        return self._nome_completo
    
    
    @nome_completo.setter
    def nome_completo(self, value):
        self._nome_completo = value
    
    
    @nome_completo.deleter
    def nome_completo(self):
        self._nome_completo = ''

