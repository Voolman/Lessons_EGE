f = open('7.txt').readlines()

a = [int(y) for y in f]
b = sum([u for u in a if u < 0])
k = 0
n = []
for i in range(len(a)-2):
    t1,t2,t3 = a[i], a[i+1], a[i+2]
    if max(t1,t2,t3)*min(t1,t2,t3) > b:
        k += 1
        n.append(t1+t2+t3)

print(k, abs((max(n))))