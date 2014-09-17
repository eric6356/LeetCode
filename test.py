ks = dict()
ks['a'] = {1, 2}
if 'b' not in ks:
    ks['b'] = set()
ks['b'].add(1)
ks['a'].add(2)
print ks['a'], ks['b']
print len(ks['a'])