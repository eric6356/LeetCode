class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        num = [2, 3, 4, 5, 1]
        start = 0
        end = len(num) - 1
        if num[start] <= num[end]:
            return num[start]
        while end - start > 1:
            mid = (end+start)/2
            if num[mid] > num[start]:
                start = mid
            else:
                end = mid
        return min(num[start], num[end])

