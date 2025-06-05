f = open('4.txt').readlines()

a = [int(y) for y in f]

b = max([u for u in a if u%100 == 15])

k = 0
n = []
for i in range(len(a)-2):
    t1,t2,t3 = a[i],a[i+1],a[i+2]
    if ( (999 < t1 < 10000) + (999 < t2 < 10000) +  (999 < t3 < 10000)) == 1 and t1+t2+t3 >= b:
        k+=1
        n.append(t1+t2+t3)
print(k, max(n))