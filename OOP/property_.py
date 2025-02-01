#Exemplo 1
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


#Exemplo 2
class ItemPedido:
    def __init__(self, desc, pr_unit, qtd):
        self.desc = desc
        self.pr_unit = pr_unit
        self.qtd = qtd


    @property
    def total(self):
        return self.pr_unit * self.qtd
    

    @property
    def qtd(self):
        return self.__qtd
    

    @qtd.setter
    def qtd(self, valor):
        if valor < 1:
            raise ValueError('Quantidade < 1')
        
        else:
            self.__qtd = valor


# Ao passar o agumento qtd na instancia de ItemPedido,
# será executado o setter da property qtd, em vez do self.qtd do __init__.
item = ItemPedido('Bike', 600, qtd=2)
