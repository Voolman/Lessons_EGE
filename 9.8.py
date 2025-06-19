from math import *
def g(x):
    s1 = []
    s2 = []
    for i in x:
        if x.count(i) > 1:
            s1.append(i)
        else:
            s2.append(i)
    return s1,s2

def f(y):
    if y[0] % 2 == 0 and y[1] % 2 != 0 and y[2] % 2 == 0 and y[3] % 2 != 0 and y[4] % 2 == 0 and y[5] % 2 != 0 and y[6] % 2 == 0:
        return True
    if y[0] % 2 != 0 and y[1] % 2 == 0 and y[2] % 2 != 0 and y[3] % 2 == 0 and y[4] % 2 != 0 and y[5] % 2 == 0 and y[6] % 2 != 0:
        return True
    return False

k = 0
l = 0
for z in open('8.csv'):
    k+=1
    m = [int(x) for x in z.split(';')]
    if f(m):
        t1, t2 = g(m)
        if sum(t2)*3 >= prod(t1):
            l += k
print(l)