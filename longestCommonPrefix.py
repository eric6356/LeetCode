def longestCommonPrefix(strs):
    if not strs:
        return ''
    i = 0
    b = 0
    for i in range(len(strs[0])):
        for st in strs:
            if len(st) <= i:
                b = 1
                break
            if st[i] != strs[0][i]:
                b = 1
                break
        if b == 1:
            break
        i += 1
    return strs[0][:i]

print longestCommonPrefix(["aaa", "aaaaa", "a"])