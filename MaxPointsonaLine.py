import random


class Point(object):
    def __init__(self, (a, b)):
        self.x = a
        self.y = b


points = list()
# for i in range(10):
# points.append(Point(random.randint(0, 9), random.randint(0, 9)))
# print points[i].x, points[i].y
pl0 = [(40, -23), (9, 138), (429, 115), (50, -17), (-3, 80), (-10, 33), (5, -21), (-3, 80), (-6, -65), (-18, 26),
       (-6, -65), (5, 72), (0, 77), (-9, 86), (10, -2), (-8, 85), (21, 130), (18, -6), (-18, 26), (-1, -15), (10, -2),
       (8, 69), (-4, 63), (0, 3), (-4, 40), (-7, 84), (-8, 7), (30, 154), (16, -5), (6, 90), (18, -6), (5, 77),
       (-4, 77),
       (7, -13), (-1, -45), (16, -5), (-9, 86), (-16, 11), (-7, 84), (1, 76), (3, 77), (10, 67), (1, -37), (-10, -81),
       (4, -11), (-20, 13), (-10, 77), (6, -17), (-27, 2), (-10, -81), (10, -1), (-9, 1), (-8, 43), (2, 2), (2, -21),
       (3, 82), (8, -1), (10, -1), (-9, 1), (-12, 42), (16, -5), (-5, -61), (20, -7), (9, -35), (10, 6), (12, 106),
       (5, -21), (-5, 82), (6, 71), (-15, 34), (-10, 87), (-14, -12), (12, 106), (-5, 82), (-46, -45), (-4, 63),
       (16, -5), (4, 1), (-3, -53), (0, -17), (9, 98), (-18, 26), (-9, 86), (2, 77), (-2, -49), (1, 76), (-3, -38),
       (-8, 7), (-17, -37), (5, 72), (10, -37), (-4, -57), (-3, -53), (3, 74), (-3, -11), (-8, 7), (1, 88), (-12, 42),
       (1, -37), (2, 77), (-6, 77), (5, 72), (-4, -57), (-18, -33), (-12, 42), (-9, 86), (2, 77), (-8, 77), (-3, 77),
       (9, -42), (16, 41), (-29, -37), (0, -41), (-21, 18), (-27, -34), (0, 77), (3, 74), (-7, -69), (-21, 18),
       (27, 146), (-20, 13), (21, 130), (-6, -65), (14, -4), (0, 3), (9, -5), (6, -29), (-2, 73), (-1, -15), (1, 76),
       (-4, 77), (6, -29)]
pl = [(0, 0)]
pl1 = [(0, 0), (0, 1)]
pl2 = [(0, -12), (5, 2), (2, 5), (0, -5), (1, 5), (2, -2), (5, -4), (3, 4), (-2, 4), (-1, 4), (0, -5), (0, -8),
       (-2, -1), (0, -11), (0, -9)]
pl3 = [(4, 0), (4, -1), (4, 5)]

for p in pl3:
    points.append(Point(p))

# print
# mx = 0
# n = len(points)
# sm = range(n)
# for i in xrange(n):
# for j in xrange(i + 1, n):
# if points[i].x - points[j].x and points[i].y - points[j].y:
#             mt = 2
#             for k in xrange(n):
#                 if k != i and k != j and (points[j].x - points[k].x) * (points[i].y - points[k].y) == (
#                             points[j].y - points[k].y) * (points[i].x - points[k].x):
#                     mt += 1
#                     print points[i].x, points[i].y
#                     print points[j].x, points[j].y
#                     print points[k].x, points[k].y
#                     print mt
#                     print ''
#             if mt > mx:
#                 mx = mt
# print 'max:', mx

mx = 0
n = len(points)
if n:
    mx = 1
ks = dict()
for i in xrange(n):
    mt = 1
    for j in xrange(i + 1, n):
        if points[j].x == points[i].x:
            mt += 1
    if mt > mx:
        mx = mt
for i in xrange(n):
    for j in xrange(i + 1, n):
        if points[i].x - points[j].x:
            k = float(points[i].y - points[j].y) / (points[i].x - points[j].x)
            b = points[i].y - k * points[i].x
            key = str(k) + str(b)
            print i, j
            print k, b, key
            print
            if not key in ks:
                ks[key] = set()
            ks[key].add(i)
            ks[key].add(j)
for key in ks:
    l = len(ks[key])
    if l > mx:
        mx = l
print 'max:', mx