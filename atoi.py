def atoi( str):
        if not str:
            return 0
        i = 0
        res = list()
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            if str[i] == '-' or str[i] == '+':
                if i == len(str) or ord(str[i+1]) < 48 or ord(str[i+1]) > 57:
                    return 0
                res.append(str[i])
                i += 1
                break
            if ord(str[i]) < 48 or ord(str[i]) > 57:
                return 0
            else:
                break
        for j in range(i, len(str)):
            if ord(str[j]) < 48 or ord(str[j]) > 57:
                break
            res.append(str[j])
        if res:
            r = int(''.join(res))
            if r > 2147483647:
                return 2147483647
            if r < -2147483648:
                return -2147483648
            return r
        return 0
a = '1'
print atoi('+1')