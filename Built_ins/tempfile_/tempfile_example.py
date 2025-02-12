import tempfile
from tempfile import TemporaryFile, TemporaryDirectory, NamedTemporaryFile
from pathlib import Path


tempfile.gettempdir() # Retorna o nome da pasta padrao de arquivos temporarios

tempfile.tempdir = '.cache' # Muda o path padrao de arquivos temporarios


# Cria um arquivo temporario "sem nome" e extensao
with TemporaryFile(mode='w+') as temp_file:
    temp_file.write('Isso é um teste')
    temp_file.seek(0)
    print(temp_file.read())


# Cria uma pasta temporaria no diretorio padrao para temporarios
# do sistema operacional, e deleta tudo que estiver na pasta no fim 
# do gerenciador de contexto.
with TemporaryDirectory() as temp_dir:
    arquivo = Path(temp_dir) / 'teste.txt'
    arquivo.write_text('Isso é um teste')

    
# Cria um arquivo temporario com NOME, podendo especificar um suffix(extensão)
# e um prefix 
with NamedTemporaryFile(suffix='.png', prefix='t') as file:
    print(file.name)

# Diz explicitamente que o arquivo temporario nao sera deletado.
with NamedTemporaryFile(delete=False) as file:
    ...