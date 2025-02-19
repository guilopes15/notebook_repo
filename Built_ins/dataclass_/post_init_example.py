from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    telefone: dict[str, str]
    ddd: int
    nome_completo: str = None


    # executa o post_init depois que os atributos sejam passados 
    # para a dataclass. O nome_completo inicia como None por defaut, entao
    # preenchemos apos a inicialização.
    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


