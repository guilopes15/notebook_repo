tabela = (
    'Palmeiras',
    'Inter',
    'Fluminense',
    'Corinthians',
    'Flamengo',
    'Athletico-PR',
    'Atlético-MG',
    'Fortaleza',
    'São Paulo',
    'América-MG',
    'Botafogo',
    'Santos',
    'Goiás',
    'Red Bull Bragantino',
    'Coritiba',
    'Cuiabá',
    'Ceará',
    'Atlético-GO',
    'Avaí',
    'Juventude',
)

print(
    f"""{'-'*50}\nLista de times do brasileirão 2022: {tabela}
{'-'*50}\n Os 5 primeiros são: {tabela[:5]}
{'-'*50}\n Os 4 ultimos são: {tabela[-4:]}
{'-'*50}\n Times em ordem alfabética: {sorted(tabela)}
{'-'*50}\n O Flamengo está na {tabela.index('Flamengo')+1}ª posição."""
)
