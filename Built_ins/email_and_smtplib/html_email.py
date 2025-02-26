from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path


msg = EmailMessage()
msg['From'] = 'guilhermemendonca25@gmail.com'
msg['To'] = 'guilherme-lopes58@hotmail.com'
msg['Subject'] = 'Teste de email com imagem'

# Criar um ID único para a imagem
imagem_cid = make_msgid()

# O slice é para remover os <> do inicio e fim da image_cid
html = f"""
<html>
  <body>
    <h1>Olá!</h1>
    <p>Este é um e-mail <b>formatado</b> com HTML.</p>
    <br>
    <h2>Imagem Embutida</h2>
    <img src="cid:{imagem_cid[1:-1]}" alt="Imagem">
  </body>
</html>
"""

# Adicionando HTML ao email
msg.add_alternative(html, subtype='html')

image_path = Path(__file__).parent / 'pocao.png'

# Adicionando a imagem ao email
with open(image_path, 'rb') as img:
    msg.get_payload()[0].add_related(
        img.read(), maintype='image', subtype='png', cid=imagem_cid
    )


