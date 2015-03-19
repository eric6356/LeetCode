# coding:utf-8
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        low = 0
        for low in range(n):
            # low是第一个不为0的
            if A[low] != 0:
                break
        high = low + 1
        while high <= n-1:
            # high是low后第一个0
            if A[high] == 0:
                break
            high += 1
        while high <= n-1:
            tmp = A[low]
            A[low] = A[high]
            A[high] = tmp
            while A[low] == 0 and low <= n-1:
                low += 1
            high = low+1
            while high <= n-1:
                # high是low后第一个0
                if A[high] == 0:
                    break
                high += 1

        high = n-1
        while high >= 0 and A[high] == 2:
            high -= 1
        low = high - 1
        while low >= 0 and A[low] == 1:
            low -= 1
        while low >= 0 and A[low]:
            tmp = A[low]
            A[low] = A[high]
            A[high] = tmp
            while high >= 0 and A[high] == 2:
                high -= 1
            low = high - 1
            while low >= 0:
                if A[low] == 0:
                    return A
                if A[low] == 2:
                    break
                low -= 1
        return A

arr = [2, 0, 1, 0, 1, 1, 0, 2, 1]
arr = [0, 1]
S = Solution()
print S.sortColors(arr)