a = [0,1,2,3,4]
for i in range(5,13767):
    a.append(2*i*a[i-4])
print((a[13766] - 9*a[13762])//a[13758])
