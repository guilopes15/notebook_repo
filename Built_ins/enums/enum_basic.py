from enum import Enum, StrEnum, IntEnum


# Enum garanti que apenas valores válidos sejam usados. No caso a class Status
# so pode ter os atributos ATIVO, INATIVO E SUSPENSO.
class Status(Enum):
    ATIVO = 1
    INATIVO = 3
    SUSPENSO = 3


# Apenas values do tipo str
class Cor(StrEnum):
    VERMELHO = "red"
    VERDE = "green"
    AZUL = "blue"


class HTTPStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500