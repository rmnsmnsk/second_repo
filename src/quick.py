def quick(m):

    if len(m) == 1 or len(m) == 0:
        return m

    middle = m[len(m)//2]

    m1 = []
    m2 = []
    m3 = []


    for i in m:
        if i < middle:
            m1.append(i)
        elif i == middle:
            m2.append(i)
        else:
            m3.append(i)

    left = quick(m1)
    right = quick(m3)

    return left + m2 + right
