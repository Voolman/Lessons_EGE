from itertools import *
k = 0
def f(t):
    for p in permutations(t):
        if p[0] + p[1] == p[2] + p[3]:
            return True
    return False
for i in open('4.csv'):
    m = [int(x) for x in i.split(';')]
    if (max(m) < sum(m)-max(m)) and f(m):
        k+=1
print(k)