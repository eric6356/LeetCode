def maxProduct(A):
    n = len(A)
    if n == 1:
        return A[0]
    zeros = list()
    result = min(A)
    for i in range(len(A)):
        if not A[i]:
            zeros.append(i)
    if zeros:
        result = max(result, 0)
        for i in range(len(zeros) + 1):
            if i == 0:
                st = 0
                end = zeros[i]
            elif i == len(zeros):
                st = zeros[i-1] + 1
                end = n
            else:
                st = zeros[i-1]+1
                end = zeros[i]
            result = max(result, largest(A[st:end]))
    else:
        return largest(A)
    return result

def largest(A):
    if not len(A):
        return 0
    if len(A) == 1:
        return A[0]
    result = min(A)
    neg_index = list()
    for i in range(len(A)):
        if A[i] < 0:
            neg_index.append(i)
    if not len(neg_index) & 1:
        result = 1
        for i in A:
            result *= i
        return result
    else:
        # better
        result1 = result2 = 1
        for i in A[:neg_index[-1]]:
            result1 *= i
        for i in A[neg_index[0]+1:]:
            result2 *= i
        return max(result1, result2)

print maxProduct([0, 2])