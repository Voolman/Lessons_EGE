a = [int(i) for i in open('17.txt')]
mx = max([i for i in a if i%36 == 0])
k = 0
mn = 1000000
for i in range(len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if ((x>0 + y>0 + z>0) > 1 or (x%100 ==36 + y%100 ==36 + z%100 ==36) > 1) and x+y+z <= mx:
        k += 1
        mn = (x+y+z,mn)
print(k, mn)