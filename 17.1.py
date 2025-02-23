def f(x):
    return x < 0

a = [int(i) for i in open('7526.txt')]
R = 0
for i in a:
    if abs(i) % 32 == 0:
        R += 1
k = 0
mx = 0
for i in range(len(a) -1):
    x,y = a[i:i+2]
    if ((f(x) + f(y))>0) and ((x+y) < R):
        k += 1
        mx = max(mx,x+y)
print(k,mx)
