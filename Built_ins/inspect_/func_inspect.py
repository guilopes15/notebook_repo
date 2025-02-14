import inspect
import asyncio


def exemplo(a, b=2, *args, **kwargs):
    """Isso é uma docstring"""
    print(inspect.stack()) # Obtem a pilha se chamadas de uma função
    

signature = inspect.signature(exemplo) # Pega os parametros da função

# Inspecionar detalhes dos parâmetros
for name, param in signature.parameters.items():
    print(f"Nome: {name}, Tipo: {param.kind}, Default: {param.default}")


inspect.getdoc(exemplo)  # Pega a docstring

inspect.getsource(exemplo)  # Pega o código-fonte

inspect.getmodule(exemplo) # Pega o modulo de onde a função veio

inspect.isfunction(exemplo) # Verifica se é uma função


# Obtem a lista de argumentos de uma função
inspect.getfullargspec(exemplo)


def gerador():
    yield 1

# Verifica se o objeto é um gerador
inspect.isgeneratorfunction(gerador) # True
inspect.isgenerator(gerador()) # True


async def minha_corrotina():
    pass

# Verifica se o objeto é uma corrotina
inspect.iscoroutinefunction(minha_corrotina)  # True
