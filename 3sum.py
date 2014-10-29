class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        res = list()
        # z = 0
        # for i in num:
        #     if i == 0:
        #         z += 1
        #         if z == 3:
        #             res.append([0, 0, 0])
        #             break
        # num = list(set(num))
        num.sort()
        n = len(num)
        # print num
        i = 0
        while i < n:
            big = n-1
            little = i+1
            while big > little:
                r = num[little] + num[big] + num[i]
                if r == 0:
                    res.append([num[i], num[little], num[big]])
                    little += 1
                    big -= 1
                    while big > little and num[little] == num[little-1]:
                        little += 1
                    while big > little and num[big] == num[big+1]:
                        big -= 1
                elif r > 0:
                    big -= 1
                    while big > little and num[big] == num[big+1]:
                        big -= 1
                else:
                    little += 1
                    while big > little and num[little] == num[little-1]:
                        little += 1
            i += 1
            while i<n and num[i] == num[i-1]:
                i+=1

        return res

n = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
n = [-2, 0, 1, 1, 2]
S = Solution()
print S.threeSum(n)
