def getRow(numRows):
    numRows += 1
    if numRows == 0:
        return []
    if numRows == 1:
        return [1]
    lst = [1]
    cur = [1]
    for i in range(1, numRows):
        # print "i:", i
        cur = [1]
        for j in range(1, i/2+1):
            cur.append(lst[j-1]+lst[j])
        for j in range((i+1)/2):
            cur.append(cur[(i+1)/2-j-1])
        # print cur
        lst = cur
    return cur
print getRow(3)