def canCompleteCircuit(gas, cost):
        youxiang = 0
        s = e = 0
        n = len(gas)
        if n == 1:
            if cost[0] > gas[0]:
                return -1
            return 0
        while True:
            youxiang = youxiang + gas[e] - cost[e]
            e += 1
            if e == n and youxiang >= 0:
                return 0
            if youxiang < 0:
                break
        while True:
            s += 1
            if s > n:
                return -1
            youxiang = youxiang + cost[s-1] - gas[s-1]
            if s == e+1:
                return -1
            if youxiang < 0:
                continue
            else:
                while True:
                    youxiang = youxiang + gas[e] - cost[e]
                    e += 1
                    if e == n:
                        e = 0
                    if e == s and youxiang >= 0:
                        return s
                    if youxiang < 0:
                        break

g = [4]
c = [5]
print canCompleteCircuit(g, c)