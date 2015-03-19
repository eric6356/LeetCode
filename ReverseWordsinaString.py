s = 'the sky is blue'
l = s.split()
r = list()
for i in range(len(l)):
    r.append(l[-1-i])
print ' '.join(r)