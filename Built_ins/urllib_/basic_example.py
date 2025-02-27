from urllib.request import urlopen


# GET por padrao
response = urlopen('https://tcc-madr.fly.dev/')

print(response.read().decode())

# Ignora caracteres inválidos
body = response.read().decode("utf-8", errors="ignore")  

# Substitui caracteres inválidos por "�"
body = response.read().decode("utf-8", errors="replace")  
 
# OBS: O urlopen() não lida bem com redirecionamentos (307, 308).