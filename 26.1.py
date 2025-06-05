f = open('26.txt')
a, b = f.readline().split()
a = int(a)
b = int(b)
z = [int(i) for i in f.readlines()]
z.sort()
print(z)

h = 0
mx = 0
k = 0
x = 0
while True:
    if h + z[x] > a:
        break
    else:
        h += z[x]
        k+=1
        mx = max(mx,z[x])
    x+=1
for i in range(1,25):
    if (mx + i in z):
        print('yes', i)
print(k, mx, h, a)