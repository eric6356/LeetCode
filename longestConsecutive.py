class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        res = range(min(num), max(num))
