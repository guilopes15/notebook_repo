import smtplib
from email.message import EmailMessage


msg = EmailMessage()

msg['From'] = 'guilhermemendonca25@gmail.com'
msg['To'] = 'guilherme-lopes58@hotmail.com'
msg['Subject'] = 'Test de email'
msg.set_content('Olá! Este é um e-mail enviado via Python.') # Corpo do email


print(msg.as_string())
print(msg.as_bytes())
