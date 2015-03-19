class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix[0])
        n = len(matrix)
        mini = 0
        maxi = n-1
        mid = n/2
        while mini <= maxi:
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                maxi = mid-1
            else:
                mini = mid+1
            mid = (maxi+mini)/2
        row = mid
        mini = 0
        maxi = m-1
        mid = m/2
        while mini <= maxi:
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                maxi = mid-1
            else:
                mini = mid+1
            mid = (maxi+mini)/2
        return False
S = Solution()
m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print S.searchMatrix(m, 3)