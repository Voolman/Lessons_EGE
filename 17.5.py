f = open('3.txt').readlines()

a = [int(y) for y in f]
b = sum(a)/len(a)
k = 0
n =[]
for i in range(len(a)-1):
    t1, t2 = a[i], a[i+1]
    if t1 < b and t2 < b:
        if t1 % 10 == 9 or t2%10 == 9:
            k+=1
            n.append(t1+t2)
print(k, max(n))