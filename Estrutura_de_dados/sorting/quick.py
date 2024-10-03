"""from random import randint


def quicksort(array):

    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quicksort(low) + same + quicksort(high)"""


def quicksort(array, start=0, end=None):

    if end is None:
        end = len(array)
    if start < end:
        part = partition(array, start, end)
        quicksort(array, start, part - 1)
        quicksort(array, part + 1, end)


def partition(array, start, end):
    pivot = array[end]
    low_index = start

    for current_index in range(start, end):

        if array[current_index] <= pivot:
            array[current_index], array[low_index] = (
                array[low_index],
                array[current_index],
            )
            low_index += 1

    array[low_index], array[end] = array[end], array[low_index]
    return low_index
