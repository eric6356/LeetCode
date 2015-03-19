def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    ans = [[1]]
    for i in range(1, numRows):
        # print "i:", i
        cur = [1]
        for j in range(1, i/2+1):
            cur.append(ans[i-1][j-1]+ans[i-1][j])
        for j in range((i+1)/2):
            cur.append(cur[(i+1)/2-j-1])
        # print cur
        ans.append(cur)
    return ans
print generate(3)