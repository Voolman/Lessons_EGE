from itertools import *
def f(x):
    for y in permutations(x):
        if x.count(y[0]) == 3 and x.count(y[1]) == 3 and x.count(y[2]) == 3 and x.count(y[3]) == 2 and x.count(y[4]) == 2 and x.count(y[5]) == 1 and x.count(y[6]) == 1:
            return [y[0],y[1],y[2],y[3],y[4],y[5],y[6]]
    return []

k = 0
for i in open('7.csv'):
    m = [int(x) for x in i.split(';')]
    s = f(m)
    if s:
        if s[0] + s[3] >= s[5] + s[6]:
            k+=1
print(k)



