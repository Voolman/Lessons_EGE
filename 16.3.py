a = [1]*2029
for i in reversed(range(2025)):
    a[i] = i - a[i+2] - a[i+4]
print(a[20]+a[25])