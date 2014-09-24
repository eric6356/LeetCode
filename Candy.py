# class Solution:
# # @param ratings, a list of integer
#     # @return an integer
def candy(ratings):
        if not ratings:
            return 0
        n = len(ratings)
        if n == 1:
            return 1
        if n == 2:
            if ratings[0] == ratings[1]:
                return 2
            return 3
        candys = [0] * n
        result = 0
        min_index = list()
        mmm = [0] * len(ratings)
        if ratings[0] < ratings[1]:
            candys[0] = 1
            result += 1
            mmm[0] = -1
            min_index.append(0)
        if ratings[-1] < ratings[-2]:
            candys[-1] = 1
            result += 1
            mmm[-1] = -1
            min_index.append(n - 1)
        for i in range(1, n - 1):
            if ratings[i - 1] >= ratings[i] <= ratings[i + 1]:
                candys[i] = 1
                result += 1
                mmm[i] = -1
                min_index.append(i)
            elif ratings[i - 1] <= ratings[i] >= ratings[i + 1]:
                mmm[i] = 1
        for index in min_index:
            # before index
            left_index = index - 1
            while left_index > 0:
                if not candys[left_index]:
                    candys[left_index] = candys[left_index+1] + 1
                    result += candys[left_index]
                    if mmm[left_index] == 1:
                        break
                    else:
                        left_index -= 1
                        continue
                if mmm[left_index] == -1:
                    break
                print 'left wrong'
                break
            # after index
            right_index = index + 1
            while right_index < n-1:
                if not candys[right_index]:
                    candys[right_index] = candys[right_index-1] + 1
                    result += candys[right_index]
                    if mmm[right_index] == 1:
                        break
                    else:
                        right_index += 1
                        continue
                if mmm[right_index] == -1:
                    break
                else:
                    if candys[right_index] <= candys[right_index-1]:
                        result += candys[right_index-1] - candys[right_index] + 1
                        candys[right_index] = candys[right_index-1] + 1

                    break
        if not candys[0]:
            if ratings[0] > ratings[1]:
                candys[0] = candys[1] + 1
                result += candys[1] + 1
            else:
                candys[0] = 1
                result += 1
        if not candys[-1]:
            if ratings[-1] > ratings[-2]:
                candys[-1] = candys[-2] + 1
                result += candys[-2] + 1
            else:
                candys[-1] = 1
                result += 1
        return result


r = [1, 2, 2]
print candy(r)