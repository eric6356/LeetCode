def wordbreak(s, dict):
    if not dict:
        return False
    n = len(s)
    dp = list()
    for i in range(n):
        dp.append([])
    for i in range(n):
        if s[:i+1] in dict:
            dp[i].append(-1)
    i = 0
    while i < n-1:
        for k in range(i+1):
            if dp[i-k] and s[i-k+1:i+2] in dict:
                dp[i+1].append(i-k)
        i += 1
    if dp[-1]:
        result = list()
        stk = list()
        order_result = list()
        for x in ooxx(dp, len(a)-1, stk, order_result):
            tmp = ''
            for i in x:
                if i > -1:
                    tmp += s[j+1:i+1] + ' '
                j = i
            tmp += s[i+1:]
            result.append(tmp)
        return result
    else:
        return False


def ooxx(_a, _index, _stk, _result):
    for x in _a[_index]:
        if x > -1:
            _stk.append(x)
            ooxx(_a, x, _stk, _result)
            _stk.pop()
        else:
            tmp = [-1]
            for i in range(len(_stk)):
                tmp.append(_stk[len(_stk) - i - 1])
            _result.append(tmp)
    return _result

a = 'aaaaaa'
d = {'aaaa', 'aa'}
print wordbreak(a, d)