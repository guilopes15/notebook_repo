# Listar a pasta_0, que esta dentro da pasta files, casp existam arquivos.txt
# dentro da pasta_0, crie uma nova pasta chamada desafio, 
# e copie os arquivos para essa pasta.
from pathlib import Path
from shutil import rmtree


output_path = Path('Built_ins/Pathlib_/desafio_2')

if output_path.exists():
    rmtree(output_path, ignore_errors=True)

output_path.mkdir()

for file_ in Path('files/pasta_0').glob('*.txt'):
    new_file = output_path / file_.name
    new_file.write_text(file_.read_text())
