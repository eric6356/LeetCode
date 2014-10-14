def removeElement(A, elem):
    i = 0
    while True:
        while A[i] == elem:
            if i == len(A)-1:
                A.pop()
                break
            A[i] = A[-1]
            A.pop()
        i += 1
        if i == len(A):
            break
    return len(A)