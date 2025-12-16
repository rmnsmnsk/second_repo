def bubble(arr):
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        for j in range(n - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy
