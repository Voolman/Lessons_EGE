f = open('6.txt').readlines()

a = [int(y) for y in f]

b = len([t for t in a if (9 < t < 100)])

k = 0
n = []
for i in range(len(a)-1):
    t1,t2 = a[i],a[i+1]
    if (t1%10) + (t2%10) == b:
        k+=1
        n.append(t1+t2)
print(k, min(n))