# Crie 10 arquivos com o nome "live_n.txt" onde n é numero do arquivo e delete
# os arquivos em que o valor é menor ou igual a 5. Quando isso estiver feito,
# renomeie os arquivos de 6 a 10 , para 1 a 5.
import os
from pathlib import Path
import shutil


for index in range(1, 11):
    Path(f'Built_ins/Pathlib_/live_{index}.txt').touch()

l_dir = [
    file for file in os.listdir('Built_ins/Pathlib_') 
    if file.startswith('live_')
]


for file in l_dir:
    if int(file.split('_')[1].split('.')[0]) <= 5:
        os.remove(f'Built_ins/Pathlib_/{file}')

l_dir = [file for file in os.listdir('Built_ins/Pathlib_') if file.startswith('live_')]

print(l_dir)

#for index, item in enumerate(sorted(l_dir)):
#    print(Path(f'Built_ins/Pathlib_/{item}').rename(f'live_{index}'))

for index, item in enumerate(sorted(l_dir)):
    shutil.move(
        os.path.join('Built_ins/Pathlib_/', item),
        f'Built_ins/Pathlib_/live_{index+1}'
    )