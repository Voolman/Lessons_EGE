k = 0
def f(x):
    s1 = []
    s2 = []
    for y in x:
        if x.count(y)>1:
            s1.append(y)
        else:
            s2.append(y)
    return s1,s2
k = 0
for i in open('9.csv'):
    l = 0
    m = [int(x) for x in i.split(';')]
    if max(m)*min(m) < (sum(m)-max(m)-min(m))*3:
        l+=1
    t1,t2 = f(m)
    if sum(t2) <= sum(t1):
        l+=1
    if l == 1:
        k += 1
print(k)