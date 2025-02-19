from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    telefone: dict[str, str]
    ddd: int

