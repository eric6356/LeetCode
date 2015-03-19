class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num.sort()
        m = 0
        tmp = 0
        for i in range(len(num)-1):
            if num[i+1] == num[i] + 1:
                tmp += 1
            elif num[i+1] == num[i]:
                pass
            else:
                m = max(m, tmp)
                tmp = 0
        return max(m, tmp) + 1