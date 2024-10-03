print('-=' * 20)
print('Analisador de triangulos')
print('-=' * 20)
p = float(input('Primeiro segmento:'))
s = float(input('Segundo segmento:'))
t = float(input('Terceiro segmneto:'))
if p + s > t:
    if p + t > s:
        if s + t > p:
            con = 'Podem formar'
else:
    con = 'Não podem formar'
print(f'Os segmentos acima {con} Triangulo.')
