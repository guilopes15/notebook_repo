from email.message import EmailMessage
from pathlib import Path


msg = EmailMessage()

msg['From'] = 'gui@example.com'
msg['To'] = 'test@test.com'
msg['Subject'] = 'Test de email'
msg.set_content('Olá! Este é um e-mail enviado via Python.') # Corpo do email


path_dir = Path(__file__).parent
with open(path_dir / 'test.txt', 'rb') as f: # Anexando um arquivo
    msg.add_attachment(
        f.read(), maintype='application', subtype='octet-stream',filename='test.txt'
    )

