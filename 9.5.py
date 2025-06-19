from itertools import *
def f(t):
    for p in permutations(t):
        if (p[0] + p[1]) == (p[2] + p[3]):
            if (p[2] + p[3]) == (p[4]+p[5]):
                return True
    return False

k = 0
for i in open('5.csv'):
    k+=1
    m = [int(x) for x in i.split(';')]
    s1= [x for x in m if x%2 == 0]
    s2= [x for x in m if x%2 != 0]
    if (len(s1) == len(s2)) and f(m):
        print(k)
