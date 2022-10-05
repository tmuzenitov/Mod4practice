def binary_search(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)
element = 33
array = [7, 2, 0, 3, 13, 9, 16, 21, 24, 28, 30, 10, 33]

print("Ищем {}".format(element))
print("Индекс {}: {}".format(element, binary_search(array, element, 0, len(array))))
