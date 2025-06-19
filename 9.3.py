from collections import *
k = 0
for i in open('3.csv'):
    m = [int(x) for x in i.split(';')]

    if len(set(m)) == 5:
        s = set()
        d = []
        for y in m:
            if y in s:
                d.append(y)
            else:
                s.add(y)
        if (sum(m)-d[0]*2)/4 >= d[0]*2:
            k+=1
print(k)