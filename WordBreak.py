def wordbreak(s, dict):
    if not dict:
        return False
    n = len(s)
    res = [False] * n
    for i in range(n):
        if s[:i+1] in dict:
            res[i] = True
    if not True in res:
        return False
    i = 0
    while i < n-1:
        for k in range(i+1):
            if res[i+1]:
                break
            if res[i-k] and s[i-k+1:i+2] in dict:
                res[i+1] = True
                break
        i += 1
    if res[-1]:
        return True
    else:
        return False

a = 'aaaaaaa'
d = {'aaaa', 'aa'}
print wordbreak(a, d)