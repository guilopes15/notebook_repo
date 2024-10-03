def notas(*numeros, situacao=False):
    """
    -> Analisa notas e situacoes de aulunos
    :param numeros: Recebe as notas
    :param situacao: Mostra ou nao a situacao (opcional)
    :return: Retorna a informacao da turma
    """
    dicionario = {}
    dicionario['total'] = len(numeros)
    dicionario['maior'] = max(numeros)
    dicionario['menor'] = min(numeros)
    dicionario['media'] = sum(numeros) / len(numeros)
    if situacao:
        if dicionario['media'] >= 7:
            dicionario['situacao'] = 'Boa'
        elif dicionario['media'] < 5:
            dicionario['situacao'] = 'Ruim'
        else:
            dicionario['situacao'] = 'Razoavel'
    return dicionario


resp = notas(5, 9, 7.5)
print(resp)

#todo o parametro *numero empacotado retorna tupla



