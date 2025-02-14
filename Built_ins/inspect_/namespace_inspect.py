import inspect
import os
from Built_ins.inspect_.func_inspect import exemplo

inspect.getfile(os) # Path para o modulo especificado

inspect.getsourcefile(exemplo) # Caminho de onde a função veio


# python -m Built_ins.inspect_.namespace_inspect

#import sys

# Adiciona o diretório raiz 'notebook_repo' ao sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
