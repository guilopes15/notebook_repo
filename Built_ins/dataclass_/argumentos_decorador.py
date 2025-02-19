from dataclasses import dataclass


@dataclass(
    init=True, 
    repr=True, 
    eq=True, 
    order=False, 
    unsafe_hash=False, 
    frozen=True
)
class Pessoa:
    nome: str
    sobrenome: str
    telefone: dict[str, str]
    ddd: int
