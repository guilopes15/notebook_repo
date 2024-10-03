print('=' * 15, 'LOJA DO GUI', '=' * 15)
price = float(input('Preço das compras: R$'))
print(
    """Formas de Pagamento
[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão"""
)
op = int(input('Qual é a opção?'))
if op == 1:
    print(
        f'Sua compra de {price:.2f} vai custar {price - (price*0.1):.2f } no dinheiro.'
    )
elif op == 2:
    print(
        f'Sua compra de {price:.2f} vai custar {price*0.95:.2f} a vista no cartão.'
    )
elif op == 3:
    calc = price / 2
    print(f'Sua compra será parcelada em 2x de R${calc:.2f} sem juros.')
elif op == 4:
    parcelas = int(input('Quantas parcelas?'))
    calc = (price * 1.2) / parcelas
    print(
        f"""Sua compra será parcelada em {parcelas}x de R${calc:.2f} com juros.
Sua compra de {price:.2f} vai custar {price * 1.2:.2f} no final."""
    )
else:
    print('Opção invalida')
