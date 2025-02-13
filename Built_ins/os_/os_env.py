import os


os.environ['HOME'] # Pega uma variavel de ambiente do sistema


# Pega uma variavel de ambiente, se nao existir retorna
# a mensagem 'Nao encontrado'.
os.environ.get('SHELL', 'Nao encontrado')
os.getenv("MINHA_VARIAVEL", "valor padrão")


# Criando uma variavel de ambiente
os.environ['MEU_APP'] = 'Dev Mode'


# Remove uma variavel de ambiente
del os.environ['MEU_APP']
os.unsetenv("TEMP_VAR")
