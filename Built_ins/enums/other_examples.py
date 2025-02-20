from enum import Enum, auto, unique, Flag


# auto atribui valores começando em 1 por padrão.
class DiaSemana(Enum):
    SEGUNDA = auto()
    TERCA = auto()
    QUARTA = auto()

DiaSemana.SEGUNDA.value  # 1
DiaSemana.TERCA.value    # 2
DiaSemana.QUARTA.value   # 3


@unique
class CodigoErro(Enum): # Garanti que não existam valores duplicados.
    ERRO_404 = 404
    ERRO_500 = 500
    ERRO_403 = 403


# Representa combinações de valores usando operadores bitwise (|, &, ~).
class Permissoes(Flag):
    LER = auto()
    ESCREVER = auto()
    EXECUTAR = auto()


minhas_permissoes = Permissoes.LER | Permissoes.ESCREVER