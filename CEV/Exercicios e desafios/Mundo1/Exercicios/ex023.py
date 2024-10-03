num = int(input('Informe um numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero {num}')
print(
    f"""unidade {u}
dezena: {d}
centena: {c}
milhar: {m}"""
)

# formula - divisão inteira pela u/d/c/m, depois resto da divisão por 10
# Ex: A dezena de 123 == 123//10 == 12 depois /10'(%10)' == 1,2 ==  o resto da divisão 2 #
