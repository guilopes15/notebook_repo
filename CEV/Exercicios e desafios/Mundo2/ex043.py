peso = float(input('Qual o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f} ')
if imc < 18.5:
    status = 'Abaixo do peso normal'
elif 18.5 <= imc < 25:
    status = 'no Peso ideal'
elif 25 <= imc < 30:
    status = 'com Sobrepeso'
elif 30 <= imc < 40:
    status = 'em Obesidade'
else:
    status = 'em Obesidade mórbida, cuidado'
print(f'Vc está {status}.')
