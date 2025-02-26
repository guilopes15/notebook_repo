import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()

msg = EmailMessage()

msg['From'] = os.getenv('SENDER')
msg['To'] = os.getenv('RECEIVER')
msg['Subject'] = 'Test de email'
msg.set_content('Olá! Este é um e-mail enviado via Python.') # Corpo do email

servidor_smtp = 'smtp.gmail.com'
porta = 587

with smtplib.SMTP(servidor_smtp, porta) as server: 
    server.starttls()
    
    email = os.getenv('SENDER')
    senha = os.getenv('PASSWORD')
    server.login(email, senha)

    remetente = email
    destinatario = os.getenv('RECEIVER')

    server.sendmail(remetente, destinatario, msg.as_string())


# site apara configurar a senha de app para habilitar o SMTP
# https://myaccount.google.com/apppasswords