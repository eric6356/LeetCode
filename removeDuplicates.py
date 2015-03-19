class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 1:
            return n
        i = 0
        j = 1
        while j < len(A):
            if A[j] != A[j-1]:
                A[i+1] = A[j]
                i += 1
            j += 1
        return i+1