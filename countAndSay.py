class Solution:
    def nt(self, s):
        lst = (0, s[0])
        res = list()
        i = 0
        for i in range(len(s)):
            if s[i] != lst[1]:
                res.append(str(i-lst[0]))
                res.append(lst[1])
                lst = (i, s[i])
        res.append(str(i-lst[0]+1))
        res.append(lst[1])
        return res
    # @return a string
    def countAndSay(self, n):
        res = '1'
        for i in range(n-1):
            res = str(''.join(self.nt(res)))
        return res
        