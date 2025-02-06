# Crie 10 pastas com o nome "pasta_n" e dentro de cada pasta crie dois
# 'arquivos_x'. Exiba toda a estrutura do diretorio.
import os
from pathlib import Path


base_path = 'Built_ins/Pathlib_'

for index in range(1, 11):
    if not os.path.exists(f'{base_path}/pasta_{index}'):
        os.mkdir(f'{base_path}/pasta_{index}')

l_dir = [
    path for path in os.listdir(base_path) 
    if os.path.isdir(os.path.join(base_path, path)) and path != 'aula_1'
]

print(l_dir)

for path in l_dir:
    Path(os.path.join(base_path, path, 'arquivo_1.txt')).touch()
    Path(os.path.join(base_path, path, 'arquivo_2.txt')).touch()

for path in os.walk(base_path):
    print(path)