class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        s = s.strip()
        if s and (s[0] == '-' or s[0] == '+'):
            s = s[1:]
        if not s:
            return False
        if s[0] == s[-1] == '.':
            return False
        if s[0] == '.':
            s = '0' + s
        if s[-1] == '.':
            s += '0'
        o9 = ord('9')
        o0 = ord('0')
        if ord(s[0]) > o9 or ord(s[-1]) > o9 or ord(s[0]) < o0 or ord(s[-1]) < o0:
            return False
        e = 0
        dian = 0
        for i in range(len(s[1:-1])):
            oi = ord(s[i+1])
            if oi == ord('e'):
                if e:
                    return False
                e = 1
                continue
            if oi == ord('.'):
                print dian
                if e or dian:
                    return False
                dian = 1
                continue
            if oi > o9 or oi < o0:
                return False
        return True
s = Solution()
a = '..2'
print s.isNumber(a)

