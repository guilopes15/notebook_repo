from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    telefone: dict[str, str] = None
    

p = Pessoa('gui', 'teste')

p_tuple = astuple(p)
p_dict = asdict(p)

pd = Pessoa(**p_dict)
