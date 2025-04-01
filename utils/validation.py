def validation(data: dict) -> bool:
    return all([
        all([value for value in data.values()]),
        data['idade'] >= 10,
        data['cpf'].isnumeric(), # Obs: rever digitos numericos
        len(data['cpf']) == 11
    ])


