def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    if len(arr) == 0:
        return arr.copy()
    
    m = arr.copy()
    n = len(m)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(m, n, i)
    
    for i in range(n - 1, 0, -1):
        m[0], m[i] = m[i], m[0]
        heapify(m, i, 0)
    
    return m
