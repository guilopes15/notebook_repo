from dataclasses import dataclass, field


# A função field nos auxilia nas escolhas e o que fazer com os atributos. 
# Vai ser carregado depois? Tem um valor padrao? se for vazio, 
# posso fazer um factory? Devo exibir esse dado na representação?
@dataclass(frozen=True)
class Pessoa:
    nome: str
    sobrenome: str
    telefone: dict[str, str] = field(default_factory=dict)
    ddd: int = field(repr=False)
    nome_completo: str = field(init=False)


    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'