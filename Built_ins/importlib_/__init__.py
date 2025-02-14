import importlib


print('Alo importlib')

def __getattr__(modulo):
    if modulo == 'functools':
        return importlib.import_module('functools')
    else:
        raise 'Import apenas functools'