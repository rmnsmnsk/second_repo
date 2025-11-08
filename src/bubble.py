def bubble(m):
    n = len(m)
    flag = True
    while flag:
        flag = False
        for j in range(n-1):
            if m[j+1] < m[j]:
                m[j], m[j+1] = m[j+1], m[j]
                flag = True
        if not flag:
            break
    return m