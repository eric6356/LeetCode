class Solution:
    def b2d(self, a):
        a = int(a)
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        res = bin(int(a, 2) + int(b, 2))
        return res[2:]