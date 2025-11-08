def merge(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr)//2

    left1 = arr[:middle]
    right1 = arr[middle:]

    left2 = merge(left1) #рекурсивно продолжаю делить половинки, пока не прихожу к ед массивам
    right2 = merge(right1)

    return merge_half(left2, right2)

def merge_half(left, right):

    merged = []

    while left and right:

        el1 = left[0]
        el2 = right[0]

        if el1 > el2:
            merged.append(right.pop(0))
        else:
            merged.append(left.pop(0))

    merged.extend(left)
    merged.extend(right) #либо оба пустые, либо один из низ

    return merged


