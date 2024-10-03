def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)

    if (end - start) > 1:
        half = (end + start) // 2
        merge_sort(array, start, half)
        merge_sort(array, half, end)
        merge(array, start, half, end)


def merge(array, start, half, end):
    left = array[start:half]
    right = array[half:end]
    top_left, top_right = 0, 0

    for index in range(start, end):
        if top_left >= len(left):
            array[index] = right[top_right]
            top_right += 1

        elif top_right >= len(right):
            array[index] = left[top_left]
            top_left += 1

        elif left[top_left] < right[top_right]:
            array[index] = left[top_left]
            top_left += 1

        else:
            array[index] = right[top_right]
            top_right += 1
