# class Solution:
# # @param ratings, a list of integer
# # @return an integer
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
        candys = dict()
        # cdy = [0] * n
        result = 0
        min_index = list()
        mmm = [0] * len(ratings)
        r = 0
        l = 0
        if ratings[0] <= ratings[1]:
            result += 1
            # cdy[0] = 1
            mmm[0] = -1
            min_index.append(0)
            l = 1
        if ratings[-1] <= ratings[-2]:
            result += 1
            # cdy[-1] = 1
            mmm[-1] = -1
            min_index.append(n - 1)
            r = 1
        for i in range(1, n - 1):
            if ratings[i - 1] >= ratings[i] <= ratings[i + 1]:
                result += 1
                # cdy[i] = 1
                mmm[i] = -1
                min_index.append(i)
            elif ratings[i - 1] <= ratings[i] >= ratings[i + 1]:
                mmm[i] = 1
        for index in min_index:
            # before index
            left_index = index - 1
            c = 1
            while left_index > 0:
                if mmm[left_index] >= 0:
                    c += 1
                    result += c
                    # cdy[left_index] = c
                    if mmm[left_index] == 1:
                        candys[left_index] = c
                        break
                    else:
                        left_index -= 1
                        continue
                break
            if not l and not left_index:
                result += c + 1
                # cdy[0] = c + 1
        for index in min_index:
            # after index
            right_index = index + 1
            c = 1
            while right_index < n - 1:
                if mmm[right_index] == 0:
                    c += 1
                    result += c
                    # cdy[right_index] = c
                    right_index += 1
                    continue
                elif mmm[right_index] == 1:
                    if right_index in candys:
                        # print ratings[right_index], candys[right_index], c
                        if c >= candys[right_index]:
                            result += c - candys[right_index] + 1
                            # cdy[right_index] += c - candys[right_index] + 1
                    else:
                        c += 1
                        result += c
                        # cdy[right_index] = c
                    break
                break
            if not r and right_index == n - 1:
                result += c + 1
                # cdy[-1] = c+1
        return result


r = [58, 21, 72, 77, 48, 9, 38, 71, 68, 77, 82, 47, 25, 94, 89, 54, 26, 54, 54, 99, 64, 71, 76, 63, 81, 82, 60, 64, 29,
     51, 87, 87, 72, 12, 16, 20, 21, 54, 43, 41, 83, 77, 41, 61, 72, 82, 15, 50, 36, 69, 49, 53, 92, 77, 16, 73, 12, 28,
     37, 41, 79, 25, 80, 3, 37, 48, 23, 10, 55, 19, 51, 38, 96, 92, 99, 68, 75, 14, 18, 63, 35, 19, 68, 28, 49, 36, 53,
     61, 64, 91, 2, 43, 68, 34, 46, 57, 82, 22, 67, 89]
print candy(r)