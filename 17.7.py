f = open('5.txt').readlines()

a = [int(y) for y in f]

k = 0
n = []
for i in range(len(a)-2):
    t1,t2,t3 = a[i],a[i+1],a[i+2]
    if t1 < t2 < t3:
        k += 1
        n.append(max(t1,t2,t3) - min(t1,t2,t3))

print(k, min(n))