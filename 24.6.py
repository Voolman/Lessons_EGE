f = open('24.6.txt').readline()

f = f.split('T')
k = 0
mx = 0
for i in range(len(f)):
    for j in range(i,100+i):
        k += len(f[j]) + 1
    mx = max(mx, k)
    k = 0
print(mx)
