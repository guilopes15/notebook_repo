from collections import namedtuple


# Um tupla nomeada que se comporta como classe, 
# podendo acessar os valores como atributos
namedtuple('Classe', 'atributos')

jogador = namedtuple('Jogador', 'nome time camisa')

j = jogador('Lugao', 'esquina', 10)

j._asdict() # Retorna uma dict que mapeia os nomes

j._replace(nome='test') # Substitui os campos


