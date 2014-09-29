   # return weather s is Palindrome
def isPalindrome( s):
    n = len(s)
    return s[:n/2] == s[:(n-1)/2:-1]
def ooxx(res, index, stk, result):
    for i in res[index]:
        if i:
            stk.append(i)
            ooxx(res, i-1, stk, result)
            stk.pop()
        else:
            tmp = [0]
            for j in stk[::-1]:
                tmp.append(j)
            result.append(tmp)
    return result
# @param s, a string
# @return a list of lists of string
def partition( s):
    n = len(s)
    if not n:
        return list()
    if n == 1:
        return [s]
    res = list()
    for i in range(n):
        res.append([i])
    for i in range(n):
        for j in range(i+1, n):
            if isPalindrome(s[i:j+1]):
                res[j].append(i)
    stk = list()
    result = list()
    ok = list()
    for cut in ooxx(res, len(res)-1, stk, result):
        tmp = list()
        i_cut = 0
        for i_cut in range(1, len(cut)):
            tmp.append(s[cut[i_cut-1]:cut[i_cut]])
        tmp.append(s[cut[i_cut]:])
        ok.append(tmp)
    return ok
s = 'ab'
print partition(s)
