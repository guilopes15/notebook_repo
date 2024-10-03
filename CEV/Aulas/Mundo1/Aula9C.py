frase = 'Curso em Video Python'
frase = frase.replace('Python', 'Android')
print(frase)
print(frase.replace('Video', 'Android'))
print('-' * 100)
dividido = frase.split()
print(f'{dividido}\n{dividido[0]}\n{dividido[0][3]}')
print(len(dividido))
