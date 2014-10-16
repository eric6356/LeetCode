class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        res = A[:m]+B
        res.sort()
        for i in range(m+n):
            A[i] = res[i]