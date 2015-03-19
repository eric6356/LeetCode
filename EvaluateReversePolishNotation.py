tokens1 = ["2", "1", "+", "3", "*"]
tokens2 = ["4", "13", "5", "/", "+"]
tokens3 = ["3", "-4", "+"]
tokens4 = ["10", '6', "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens5 = ["18"]
t = tokens4
stk = list()
for o in t:
    print stk, o
    if '9' >= o[-1] >= '0':
        stk.append(float(o))
    elif o == '+':
        b = stk.pop()
        a = stk.pop()
        stk.append(int(a + b))
    elif o == '-':
        b = stk.pop()
        a = stk.pop()
        stk.append(int(a - b))
    elif o == '*':
        b = stk.pop()
        a = stk.pop()
        stk.append(int(a * b))
    else:
        b = stk.pop()
        a = stk.pop()
        stk.append(int(a / b))
print int(round(stk.pop()))