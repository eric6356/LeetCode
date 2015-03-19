class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return map(list, zip(*matrix[::-1]))

S = Solution()
print S.rotate([[1, 2], [3, 4], [5, 6]])
