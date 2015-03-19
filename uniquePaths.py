class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        m-=1
        n-=1
        if not (m and n):
            return 1
        return reduce(lambda x, y: x*y, range(n+1, m+n+1)) / reduce(lambda x, y: x*y, range(1, m+1))

S = Solution()
print S.uniquePaths(3, 7)