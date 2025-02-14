import inspect

class Exemplo:
    def metodo(self):
        pass


inspect.isclass(Exemplo) # Verifica se é uma classe

# Verifica se é um metodo
inspect.ismethod(Exemplo.metodo) # False
inspect.ismethod(Exemplo().metodo) # True

inspect.getmro(Exemplo)  # Mostra a hierarquia de herança da classe