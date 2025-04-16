c = float(input('Informe a temperatura em Cº:'))
cf = c * 1.8 + 32
print(f'A temperatura de {c}Cº corresponde a {cf}Fº!')
f = float(input('Informe a temperatura em Fº'))
fc = (f - 32) * 5 / 9
print(f'A tem temperatura de {f}Fº corresponde a {fc:.2f}Cº')

# formula de Cº para Fº - (Cº*9/5)+32
# formula de Fº para Cº - (Fº-32)*5/9
