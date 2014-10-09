def longestConsecutive(num):
        num.sort()
        m = 0
        tmp = 0
        for i in range(len(num)-1):
            if num[i+1] == num[i] + 1:
                tmp += 1
            elif num[i+1] == num[i]:
                pass
            else:
                m = max(m, tmp)
                tmp = 0
        return max(m, tmp) + 1

num = [100, 4, 200, 1, 3, 2]
num2 = [1, 2, 0, 1]
num3 = [1, 3, 5, 2, 4]
print longestConsecutive(num)
print longestConsecutive(num2)
print longestConsecutive(num3)
print longestConsecutive([0,3,7,2,5,8,4,6,0,1])