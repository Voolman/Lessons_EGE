f = open('24.3.txt').readline()

a = []
for i in range(len(f)):
    if f[i] not in '123456789ABCDEF': continue
    r = i
    while f[r] in '0123456789ABCDEF':
        r += 1
    a.append(r-i)
print(max(a))