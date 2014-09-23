   # @param A, a list of integer
# @return an integer
def singleNumber(A):
    dic_p = dict()
    dic_n = dict()
    for num in A:
        if num > 0:
            i_b_p = bin(num)[2:]
            for j in range(len(i_b_p)):
                if j in dic_p:
                    dic_p[j] += int(i_b_p[len(i_b_p)-j-1])
                else:
                    dic_p[j] = int(i_b_p[len(i_b_p)-j-1])
        else:
            i_b_n = bin(num)[3:]
            for j in range(len(i_b_n)):
                if j in dic_n:
                    dic_n[j] += int(i_b_n[len(i_b_n)-j-1])
                else:
                    dic_n[j] = int(i_b_n[len(i_b_n)-j-1])
    result_p = 0
    result_n = 0
    for (key, val) in dic_p.items():
            result_p <<= 1
            result_p += (val % 3)
    for (key, val) in dic_n.items():
            result_n <<= 1
            result_n += (val % 3)
    return result_n | result_p


a = [0, 0, 0, 5]
print singleNumber(a)