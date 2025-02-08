import shutil


# Copia o arquivo dados para backup_dados
shutil.copy('dados.csv', 'backup_dados.csv') 

# Copia o arquivo dados para backup_dados perservando os metadados
shutil.copy2('dados.csv', 'backup_dados.csv') 

#copia recursivamente todo o diretorio de origem para o destino
shutil.copytree('pasta_origem', 'pasta_destino')

# Remove um diretorio recursivamente 
shutil.rmtree('pasta_para_remover', ignore_errors=True)

# Move o arquivo ou pasta da origem para o destino
shutil.move('pasta_origem', 'pasta_destino')

# Compacta um diretorio da origem para o destino, especificando o formato
shutil.make_archive('arquivo_compactado', 'zip', 'pasta_a_comprimir')

# Extrai um arquivo compactado do o destino
shutil.unpack_archive('arquivo_compactado.zip', 'pasta_destino')

# Retorna uma tupla com o uso de disco em bytes
shutil.disk_usage('.')

