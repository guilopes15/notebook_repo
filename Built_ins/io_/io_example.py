from io import StringIO, BytesIO, TextIOWrapper


# StringIO faz uma string se comportar como um arquivo. 
# Cria um buffer em memoria.
buffer = StringIO()
buffer.write('Isso é um teste')
buffer.seek(0)
print(buffer.read())
buffer.close()


# BytesIO é usado para manipular arquivos binarios, 
# criando um buffer em memoria sem precisar criar arquivos em disco.
buffer = BytesIO()
# Simulando uma imagem com Bytes
buffer.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")

with open("imagem.png", "wb") as f:
    buffer.seek(0)  
    f.write(buffer.read())
print(buffer.getvalue())


# TextIOWrapper cuida da conversão entre bytes e strings, 
# aplicando uma codificação especificada(por exemplo: utf-8).
binary_text = BytesIO(b"Texto em bytes")
text_stream = TextIOWrapper(binary_text, encoding="utf-8")
print(text_stream.read()) 