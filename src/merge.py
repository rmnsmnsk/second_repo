def merge_half(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

def merge(arr):
    if len(arr) <= 1:
        return arr.copy()
    
    middle = len(arr) // 2
    
    left = merge(arr[:middle])
    right = merge(arr[middle:])
    
    return merge_half(left, right)
