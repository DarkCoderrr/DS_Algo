#initially both the arrays will be sorted.

def intersection_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:  # arr1[i] == arr2[j]
            if not result or result[-1] != arr1[i]:  # Avoid duplicates
                result.append(arr1[i])
            i += 1
            j += 1

    return result

# Example Usage:
arr1 = [1, 2, 2, 3, 4, 5, 6]
arr2 = [2, 2, 3, 5, 7]
print(intersection_sorted_arrays(arr1, arr2))
