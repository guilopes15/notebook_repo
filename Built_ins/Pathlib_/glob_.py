from pathlib import Path

path_atual = Path()
files = path_atual / 'Built_ins' / 'Pathlib_' / 'files'
pasta_0 = files / 'pasta_0'

# Pega todos os Path de arquivos da pasta_0 que terminam com .txt
p = pasta_0.glob('*.txt') 

diretorios = [path for path in p if p.is_dir()]

print(diretorios)

# Pega todos os Path de todos os arquivos de todas as pastas
# dentro de files terminam com .txt
all_files = files.glob('**/*.txt') # O * é um wildcard que significa todos