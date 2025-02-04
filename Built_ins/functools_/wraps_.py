from functools import wraps


# O wraps serve para "organizar/injetar" o namespace 
# da função decorada para a função inner do decorador.
def func_name(func):
    @wraps
    def inner(*args):
        print(f'func_name: {func.__name__}')
        return func(*args)
    return inner


@func_name
def return_self(x):
    return x