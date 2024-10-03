def insertion_sort(array: list[int]) -> None:
    for index in range(1, len(array)):
        key = array[
            index
        ]   # aponta inicialmente para o segundo item, e depois para os itens que forem inseridos subsequente
        previous = index - 1
        while previous >= 0 and array[previous] > key:
            # percorre os itens a esquerda, comparando com o item inserido
            array[previous + 1] = array[previous]
            previous -= 1
        array[previous + 1] = key
