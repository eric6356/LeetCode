class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix[0])
        n = len(matrix)
        r_0 = [0]*m
        del_r = set()
        del_c = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    del_r.add(i)
                    del_c.add(j)
        for r in del_r:
            matrix[r] = r_0[:]
        for c in del_c:
            for i in range(n):
                matrix[i][c] = 0

S = Solution()
mx = [
    [1, 2, 3, 4, 5],
    [3, 1, 4, 0, 5],
    [1, 2, 3, 4, 5]
]
mx2 = [[1, 0]]
S.setZeroes(mx2)
print mx2

