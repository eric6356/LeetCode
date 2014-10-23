a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lie = list()
for i in range(len(a)):
    lie.append(map(lambda x:x[i], a))
print lie
blk = list()
for i in range(9):
    blk.append(list())
for d in range(3):
    for k in range(3):
        tmp = list()
        for i in range(3):
            for j in range(3):
                tmp.append((i+d*3, j+k*3))
        print tmp
