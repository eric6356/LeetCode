class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        xxx = None
        x = y = None
        for i in range(len(num)):
            if num[i] == target/2:
                if x is None:
                    x = i+1
                elif y is None:
                    return x, i+1
        n_cp = num[:]
        num.sort()
        for i in range(len(num)):
            if num[i] >= target/2:
                break
        les = num[:i]
        print les
        more = num[i:]
        print more
        l = 0
        h = len(more)-1
        while not xxx:
            # print l, h
            res = les[l] + more[h]
            if res > target:
                h -= 1
            elif res < target:
                l += 1
            else:
                xxx = num[l], num[i+h]
        for i in range(len(n_cp)):
            if n_cp[i] == xxx[0]:
                x = i+1
            if n_cp[i] == xxx[1]:
                y = i+1
        if y > x:
            return x, y
        else:
            return y, x
n = [0,4,3,0]
S = Solution()
print S.twoSum([5,75,25], 100)