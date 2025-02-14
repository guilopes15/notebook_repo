import importlib
import types

func = importlib.import_module('functools')

__import__('itertools')


# Criando um modulo em tempo de execução, sem importar
types.ModuleType('meu_modulo')
