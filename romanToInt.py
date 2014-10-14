def conv(c):
    if c == 'M':
        return 1000
    if c == 'D':
        return 500
    if c == 'C':
        return 100
    if c == 'L':
        return 50
    if c == 'X':
        return 10
    if c == 'V':
        return 5
    if c == 'I':
        return 1
def romanToInt(s):
    if len(s) == 1:
        return conv(s)
    res = 0
    for i in range(len(s)-1):
        if conv(s[i]) < conv(s[i+1]):
            res -= conv(s[i])
        else:
            res += conv(s[i])
    return res