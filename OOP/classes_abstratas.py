from abc import ABC, abstractmethod


class Forma(ABC):
    
    @abstractmethod # Obriga a subclass implementar/sobrescrever este metodo.
    def area():
        pass


    @classmethod # Um metodo que é vinculado apenas a classe. Manipula dados da propria classe.
    def tipo(cls):
        return cls.__name__
    
    
    @staticmethod # Metodo que nao depende do estado da classe nem da instancia.
    def valida_positivo(value):
        if value <= 0:
            raise ValueError("Valor deve ser positivo.")
        return value


class Circulo(Forma):   
    def __init__(self, radius):
        self.radius = radius
    
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    

c = Circulo(3)
