def x(s):
    i = 0
    j = 0
    m = 0
    a = []
    while i < len(s) and j < len(s):
        if (s[j] not in a):
            a.append(s[j])
            j = j+1
            m = max(m,j-i)
        else:
            a.remove(s[i])
            i = i+1
    return m
print(x("geeksforgeeks"))