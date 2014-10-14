def reverse(x):
    chx = str(x)[::-1]
    if chx[-1] == '-':
        return -int(chx[:-1])
    return int(x)
print reverse(-0)
