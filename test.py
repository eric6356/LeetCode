import time

# t_start = time.time()
# a = list()
# for i in range(100000):
#     a.append(i)
# for i in range(100000):
#     del a[0]
# t_1 = time.time()
# for i in range(100000):
#     a.append(i)
# for i in range(100000):
#     a.pop()
# t_2 = time.time()
# print t_1 - t_start, t_2 - t_1

t1 = time.time()
a = range(20000)
for i in range(10000, 20000):
    if i in a:
        pass
t2 = time.time()
print t2 - t1