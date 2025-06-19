f = [0]*10**13
for i in range(10**12+11):
    if i == 1:
        f[i] = 3
    else:
        f[i] = 5*f[i-1]
print(f[10**12 + 10]//(2**(5-10*11)))