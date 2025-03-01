from configparser import ConfigParser
from pathlib import Path


default_args = {
    'verbose': 0,
    'url': 'http://google.com',
    'port': 8000
}


# allow_no_values -> permite que caso uma chave seja chamada sem valor, 
# nao cause uma exceçao.

# strict -> Permite que os blocos se repitam no arquivo de configuração,
# por exemplo ter 2 args com a chave 'verbose'.
config = ConfigParser(default_args, allow_no_value=True, strict=False)

config.read(Path(__file__).parent / 'example.ini')

default_config = dict(config['default'])
secao_config = dict(config['secao_test'])

# Transforma o arg 'verbose' em int
verbose = config.getint("default", "verbose") 

# Transforma o arg 'modo_debug' em bool
modo_debug = config.getboolean("default", "modo_debug") 

print(default_config)
print(secao_config)

config.remove_option("secao_test", "test")  # Remove o arg 'test'
config.remove_section("secao_test") # Remove todas a secao 'secao_test'