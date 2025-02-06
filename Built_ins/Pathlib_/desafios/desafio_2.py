# Crie um diretorio "aula_1", caso ele nao exista, e criar um arquivo chamado
# exemplo.txt, se o arquivo já existir, vamos remover e usar o novo. A partir
# do 'exemplo.txt' vamos copiar esse arquivo em outro 3 arquivos 
# (exemplo_1.txt, exemplo_2.txt, exemplo_3.txt). Ao final, vamos listar o
# diretorio e fazer uma assertiva de que nesse diretorio só existem 4 arquivos
import os
import os.path
import shutil
from pathlib import Path


if not os.path.exists('Built_ins/Pathlib_/aula_1'):
    os.mkdir('Built_ins/Pathlib_/aula_1')

os.chdir('Built_ins/Pathlib_/aula_1') # Vai para este diretorio
os.getcwd() # mostra o diretorio atual

Path('exemplo.txt').touch()

for index in range(1, 4):
    # Copia um arquivo e cola no path desejado
    shutil.copy('exemplo.txt', f'exemplo_{index}.txt') 

# retorna na lista com todos os arquivos do diretorio atual
arquivos_aula = os.listdir('.') 

assert len(arquivos_aula) == 4