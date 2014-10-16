def merge(A, m, B, n):
    res = A[:m]+B
    res.sort()
    for i in range(m+n):
        A[i] = res[i]



A = [0, 0, 0, 0, 0]
B = [1, 2, 3, 4, 5]
m = 0
n = 5
merge(A, m, B, n)
print A, B
