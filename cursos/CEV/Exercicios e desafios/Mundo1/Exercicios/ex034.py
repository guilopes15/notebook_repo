s = float(input('Qual é o salario do funcionario? R$'))
if s > 1250:
    c = s * 1.10
else:
    c = s * 1.15
print(f'Quem ganha R${s:.2f} passa a ganhar R${c:.2f} agora.')
