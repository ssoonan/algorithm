def partition(array, low, high):
    pivot = high
    left = low
    for right in range(low, high):
        if array[right] < array[pivot]:
            array[left], array[right] = array[right], array[left]
            left += 1
    array[left], array[high] = array[high], array[left]
    return left


def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)
 
 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quickSort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)