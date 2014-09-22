def ooxx(a, index, stk, result):
    for x in a[index]:
        if x > -1:
            stk.append(x)
            ooxx(a, x, stk, result)
            stk.pop()
        else:
            tmp = [-1]
            for i in range(len(stk)):
                tmp.append(stk[len(stk) - i - 1])
            result.append(tmp)
    return result

s = 'aaaaaa'
a = [[], [], [], [], [], [-1]]
print a
stk = list()
order_result = list()
result = list()
print ooxx(a, len(a)-1, stk, order_result)
stk = list()
order_result = list()
for x in ooxx(a, len(a)-1, stk, order_result):
    tmp = list()
    for i in x:
        if i > -1:
            tmp.append(s[j+1:i+1])
        j = i
    tmp.append(s[i+1:])
    result.append(tmp)
print result
