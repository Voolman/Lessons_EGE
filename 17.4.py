f = open('2.txt').readlines()

a = [int(y) for y in f]

b = len([y for y in a if abs(y) % 100 == 0])
k = 0
mx = []
for i in range(len(a) - 1):
    t1, t2 = a[i], a[i+1]
    if (t1 < 0 or t2<0) and t1+t2 < b:
        k += 1
        mx.append(t1+t2)
print(k, abs(max(mx)))