def longestConsecutive(num):
        res = dict()
        for i in num:
            if i in res:
                continue
            if i-1 in res:
                if i+1 in res:
                    res[i-1] += res[i+1]+1
                    res[i] = res[i-1]
                    res[i+1] = res[i-1]
                    continue
                else:
                    res[i-1] += 1
                    res[i] = res[i-1]
                    continue
            elif i+1 in res:
                res[i] = res[i+1] + 1
                res[i+1] = res[i]
                continue
            else:
                res[i] = 1
        m = 0
        for i in res:
            m = max(m, res[i])
        return m

num = [100, 4, 200, 1, 3, 2]
num2 = [1, 2, 0, 1]
num3 = [1, 3, 5, 2, 4]
print longestConsecutive(num)
print longestConsecutive(num2)
print longestConsecutive(num3)
