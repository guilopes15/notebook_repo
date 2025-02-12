from tempfile import SpooledTemporaryFile


size = 1_000_000

# O SpooledTemporaryFile atua de forma dinamica, se o size do arquivo 
# for menor que o especificado ele cria um BytesIO(arquivo em memoria),
# se for maior cria um arquivo temporario.
with open('image.jpg', 'rb') as file:
    with SpooledTemporaryFile(max_size=size) as stf:
        in_memory = stf.write(file.read())
