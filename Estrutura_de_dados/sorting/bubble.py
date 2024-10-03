def bubble_sort(array: list[int]) -> None:
    for _ in range(len(array) - 1):
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
