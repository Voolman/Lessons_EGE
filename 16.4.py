f = [0]*50000
for i in range(0,50000):
    if i < 20:
        f[i] = i
    else:
        f[i] = (i-6)*f[i-7]
print((f[47872] - 290*f[47865])//f[47858])