c = float(input('Qual é o valor da casa?R$'))
s = float(input('Salario do comprador:'))
a = int(input('Quantos anos de financiamento?'))
p = c / (a * 12)
print(
    f'Para pagar uma casa de R${c:.2f} em {a} anos a prestação será de R${p:.2f}'
)
if p <= s * 0.3:
    cn = 'Concedido'
else:
    cn = 'Negado'
print(f'Emprestimo {cn}')
