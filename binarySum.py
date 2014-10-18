class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        res = list()
        jin = 0
        a = list(a)
        b = list(b)
        while a and b:
            dig = int(a.pop()) + int(b.pop()) + jin
            if dig > 1:
                jin = 1
                res.insert(0, str(dig-2))
            else:
                jin = 0
                res.insert(0, str(dig))
        if b:
            a = b
        if jin:
            while a:
                if a.pop() == '1':
                    res.insert(0, '0')
                else:
                    res.insert(0, '1')
                    jin = 0
                    break
        while a:
            res.insert(0, a.pop())
        if jin:
            res.insert(0, '1')
        return ''.join(res)
