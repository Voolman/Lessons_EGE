f = open('1.txt').readlines()
f = [int(y) for y in f]
k = 0
mn = []
for i in range(len(f)-1):
    t1, t2 = f[i], f[i+1]
    if abs(t1) % 7 == 0 or abs(t2) % 7 == 0:
        if abs(t1) % 10 == 3 or abs(t2) % 10 == 3:
            k += 1
            mn.append(t1+t2)
print(k, min(mn))