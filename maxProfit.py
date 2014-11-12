class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        mini = prices[0]
        res = 0
        for p in prices:
            mini = min(mini, p)
            res = max(res, p-mini)
        return res

S = Solution()
print S.maxProfit([1, 2])