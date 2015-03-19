# @param n, an integer
# @return an integer
def climbStairs(n):
    if n == 1:
        return 1
    n_2 = 1
    n_1 = 1
    for i in range(1, n):
        tmp = n_2
        n_2 = n_1
        n_1 += tmp
    return n_1

for i in range(10):
    print climbStairs(i)