# class Solution:
#     # @param A, a list of integer
#     # @return an integer
def singleNumber(A):
    result = 0
    for i in A:
        result ^= i
    return result

a = [1, 1, 2, 2, 3, 3, 4]
print singleNumber(a)