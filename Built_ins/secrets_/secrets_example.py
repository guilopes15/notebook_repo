import secrets


num = secrets.randbelow(100) # Gera um numero inteiro random entre 1 a 99.


# Gera um numero inteiro random de até 10 bits (0 a 1023)
num = secrets.randbits(10) 


token = secrets.token_bytes(16) # Gera 16 bytes random.


# Gera uma string hexadecimal de 16 bytes random (32 caracteres).
# Usado para cria suas secrets keys em um arquivo .env para seu app.
token = secrets.token_hex(16) 


# Gera um token seguro para ser usado em URLs
token = secrets.token_urlsafe(16) 


# Escolhe um elemento random de uma sequencia
char = secrets.choice("abcd1234") 

