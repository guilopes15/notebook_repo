import shutil


# Copia o conteúdo de um objeto de arquivo (file-like object), Essa função 
# é útil quando você já tem os arquivos abertos ou quando está trabalhando 
# com streams. 
with open('origem.txt', 'rb') as file_like_origem:
    with open('destino.txt', 'wb') as file_like_destino:
        shutil.copyfileobj(file_like_origem, file_like_destino)


# Retorna uma tupla com os formatos de arquivos que podem ser criados
# pelo make_archive.
shutil.get_archive_formats()

#Retorna uma lista de tuplas com os formatos de arquivo que podem ser descompactados 
#com a função unpack_archive()
shutil.get_unpack_formats()

