n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2
if media >= 7:
    status = 'APROVADO'
elif 5 <= media < 7:
    status = 'RECUPERAÇÂO'
else:
    status = 'REPROVADO'
print(
    f"""Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}.
O aluno está {status}."""
)

# alternativo
# elif media >= 5 and media <7:
