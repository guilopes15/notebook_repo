import zipfile


text = ''' Esse é o texto que será compactado e ...
... guardado dentro de um arquivo zip.
'''

with zipfile.ZipFile('file.zip', 'w', zipfile.ZIP_DEFLATED) as file:
    file.writestr('text.txt', text)

    file_list = file.namelist()

    for arq in file_list:
        print(f'Arquivo: {arq}')
        
        zipinfo = file.getinfo(arq)
        print('Tamanho original:', zipinfo.file_size)
        print('Tamanho comprimido:', zipinfo.compress_size)

        print(file.read(arq))

        