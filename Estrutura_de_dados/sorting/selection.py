from random import sample


def selection_sort(array: list[int]) -> None:

    for position in range(len(array) - 1):

        min_index = position
        for index in range(position, len(array)):
            if array[index] < array[min_index]:
                min_index = index

        if array[position] > array[min_index]:
            array[position], array[min_index] = (
                array[min_index],
                array[position],
            )


if __name__ == '__main__':
    lista = sample(range(0, 100), 42)
    selection_sort(lista)
    print(lista)
