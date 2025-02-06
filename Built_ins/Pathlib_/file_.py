from pathlib import Path


path_atual = Path() / 'Built_ins' / 'Pathlib_'
pasta_0 = path_atual / 'files' / 'pasta_0'
pasta_0.mkdir(parents=True, exist_ok=True) # Cria a pasta

for item in pasta_0.iterdir(): # Percorre diretorios
    print(item.name)

arquivo_0 = pasta_0 / 'arquivo_0.txt'

arquivo_0.exists() # False
arquivo_0.is_file() # False
arquivo_0.is_dir() # False

arquivo_0.touch() # Cria a arquivo

arquivo_0.exists() # True
arquivo_0.is_file() # True

arquivo_0.suffix # .txt
arquivo_0.stem # nome do arquivo -> arquivo_0

arquivo_1 = pasta_0 / 'arquivo.tar.gz'
arquivo_1.suffixes # ['.tar', '.gz']

arquivo_0.write_text('apenas um teste', encoding="utf-8")
arquivo_0.read_text(encoding="utf-8")

arquivo_renomeado = arquivo_0.rename('arquivo_renomeado')
arquivo_renomeado.unlink() # remove o arquivo
pasta_0.rmdir() # remove a pasta
