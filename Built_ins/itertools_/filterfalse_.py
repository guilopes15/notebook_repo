from itertools import filterfalse

ordens = [
    {"id": 1, "status": "pago"},
    {"id": 2, "status": "cancelado"},
    {"id": 3, "status": "pendente"},
    {"id": 4, "status": "pago"},
    {"id": 5, "status": "cancelado"},
]


def foi_pago(orden): 
    return orden["status"] == "pago"


# Retorna os valores que sao True na comparação.
ordens_pagas = filter(foi_pago, ordens) 

# Retorna os valores que sao False na comparação.
ordens_não_pagas = filterfalse(foi_pago, ordens)

