a = [int(i) for i in open('7429.txt')]
mn = 100000000
for i in a:
    if 9<i<100 and i % sum(map(int,str(i))) == 0:
        mn = min(mn,i)

k = 0
mx = 0
for i in range(len(a)-1):
    x, y = a[i:i+2]
    if x % mn == 0 or y % mn == 0:
        k+= 1
        mx = max(mx,x+y)
print(k,mx)
