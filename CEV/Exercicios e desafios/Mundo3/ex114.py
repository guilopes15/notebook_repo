import urllib.request


try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('indisponivel')
else:
    print('Ok')
    print(site.read())

#try:
#    webbrowser.open('http://pudim.com.br')
#except:
#    print('erro2')
#else:
#    print('ok2')

#todo urllib testa pra ve se o site esta no ar,
# read() visualiza o codigo html