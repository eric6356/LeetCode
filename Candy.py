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
    candys = [0] * len(ratings)
    # done means how many children have been given candy
    done = 0
    last_index = list()
    mmm = [0] * len(ratings)
    if ratings[0] < ratings[1]:
        candys[0] = 1
        done += 1
        mmm[0] = -1
        last_index.append(0)
    if ratings[-1] < ratings[-2]:
        candys[-1] = 1
        done += 1
        mmm[-1] = -1
        last_index.append(n - 1)
    for i in range(1, n - 1):
        if ratings[i - 1] > ratings[i] < ratings[i + 1]:
            candys[i] = 1
            done += 1
            mmm[i] = -1
            last_index.append(i)
        elif ratings[i - 1] < ratings[i] > ratings[i + 1]:
            mmm[i] = 1

    while done < n:
        this_indx = list()
        for index in last_index:
            # before index
            if index > 0 and candys[index - 1] == 0:
                if ratings[index - 1] > ratings[index]:
                    candys[index - 1] = candys[index] + 1
                    this_indx.append()
                else:
                    candys[index - 1] = candys[index] + 1


        last_index = this_indx
        print done
    print candys


r = [1, 2, 2]
candy(r)