class Solution:
# @return a list of integers
    def grayCode(self, n):
        num = 2**n
        return map(lambda x: (x>>1)^x, [x for x in range(num)])