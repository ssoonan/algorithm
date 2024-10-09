def merge_list(arr1, arr2):
    i, j = 0, 0
    result = []
    while (i < len(arr1) and j < len(arr2)):
        if arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            result.append(arr1[i])
            i += 1
    while (i < len(arr1)):
        result.append(arr1[i])
        i += 1
    while (j < len(arr2)):
        result.append(arr2[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_list(left, right)
 

# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print(*arr)
    arr = merge_sort(arr)
    print("\nSorted array is ")
    print(*arr)