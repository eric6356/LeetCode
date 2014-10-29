class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return
        num.sort()
        i = 0
        n = len(num)
        m = num[0] + num[1] + num[2] - target
        while i < n-1:
            little = i+1
            big = n-1
            while big > little:
                t = num[i] + num[little] + num[big] - target
                if t == 0:
                    return target
                if t > 0:
                    if m > 0:
                        m = min(m, t)
                    elif -m > t:
                        m = t
                    big -= 1
                    while big > little and num[big] == num[big+1]:
                        big -= 1
                elif t < 0:
                    if m < 0:
                        m = max(m, t)
                    elif m > -t:
                        m = t
                    little += 1
                    while big > little and num[little] == num[little-1]:
                        little += 1
            i += 1
            while i < n-1 and num[i] == num[i-1]:
                i += 1
        return target + m

s = Solution()
print s.threeSumClosest([0, 2, 1, -3], 1)