salario_hora = float(input('Quanta ganha por hora?'))
horas_mes = int(input('Trabalha quantas hrs por mes?'))
salario_bruto = salario_hora * horas_mes
impostos = {'ir': 0.11, 'inss': 0.08, 'sindicato': 0.05}
descontos = 0
for diminuir in impostos.values():
    descontos += salario_bruto * diminuir
salario_liquido = salario_bruto - descontos
print(salario_liquido)

