   # @param A, a list of integer
# @return an integer
def singleNumber(A):
    ones = 0
    twos = 0
    for i in A:
        ones ^= i & ~twos
        twos ^= i & ~ones
    return ones


a = [1, 1, 1, 2, 2, 2, 3]
print singleNumber(a)