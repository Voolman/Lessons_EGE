f = open('8.txt').readlines()

a = [int(y) for y in f]
b = min([u for u in a if abs(u) % 100 == 15 and 99 < abs(u )< 1000])**2

k = 0
n = []
for i in range(len(a) - 2):
    t1,t2,t3 = a[i], a[i+1], a[i+2]
    if (((t1 >= 0) and (t2 >= 0) and (t3 >= 0)) or ((t1 < 0) and (t2 < 0) and (t3 <0))) and max(t1,t2,t3)*min(t1,t2,t3) > b:
        k +=1
        n.append(max(t1,t2,t3)*min(t1,t2,t3))
print(k, min(n))