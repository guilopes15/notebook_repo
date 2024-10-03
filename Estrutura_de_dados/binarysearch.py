def binarysearch(array, item, start=0, end=None):
    if end == None:
        end = len(array) - 1
    if start <= end:
        mid = (start + end) // 2
        if array[mid] == item:
            return mid
        if item < array[mid]:
            binarysearch(array, item, start, mid - 1)
        else:
            binarysearch(array, item, mid + 1, end)
    return None
