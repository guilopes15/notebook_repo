v = int(input('Qual a velocidade atual do carro?'))
m = (v - 80) * 7
if v > 80:
    print(
        f"""Multado! Vc excedeu o limite de velocidade que é de 80Km/h
Vc de pagar uma multa de R${m:.2f}"""
    )
print('Tenha um bom dia! Dirija com segurança!')
