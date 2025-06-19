f = [1]*2050
for n in range(1,2050):
    if n == 1:
        f[n] = 1
    else:
        f[n] = n*f[n-1]

print((f[2024]//4 + f[2023])//f[2022])
