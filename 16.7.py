f = [0]*1000000000
k = 0
for i in range(1000000000):
    if i == 0:
        f[i] = 6
    if i % 2 == 0:
        f[i] = 1+f[i//2]
    else:
        f[i] = f[i//2]

for y in f:
    if y == 9:
        k +=1
print(k)
