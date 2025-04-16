ps = float(input('Primeiro segmento:'))
ss = float(input('Segundo segmento:'))
ts = float(input('Terceiro segmento:'))
if ps + ss > ts and ps + ts > ss and ss + ts > ps:
    cond = 'PODEM FORMAR'
    if ps == ts == ss:
        triangulo = 'EQUILÁTERO'
    elif ps == ss != ts or ps == ts != ss or ss == ts != ps:
        triangulo = 'ISÓSCELES'
    elif ps != ss != ts != ps:
        triangulo = 'ESCALENO'
    print(f'Os segmento acima PODEM FORMAR um triangulo {triangulo}')
else:
    print('Os segmento acima NÂO PODEM formar um triangulo')
