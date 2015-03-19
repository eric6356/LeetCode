class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = [[]] * (reduce(lambda x,y:x*y, range(3, n+1), 1) / reduce(lambda x,y:x*y, range(1, k+1), 1))
        print resx


s = Solution()
s.combine(4, 2)
