f = open('24.1000.txt').readline()

L = 0
R = 0
k = 0
mx = []
while L < len(f):
    while R < len(f) and k < 81:
        if f[R:R+5] == 'ADOBE':
            k += 1
        if k == 81:
            mx.append(f[L:R+4])
        R += 1
    while L < len(f) and f[L:L+5] != 'ADOBE':
        L += 1
    L += 1
    k -= 1
c = []
print('---------------')
for i in mx:
    a = i
    while a.count('EE') > 0:
        a = a.replace('EE', 'E E')
    a = a.split(' ')
    for j in a:
        c.append(len(j))
print(max(c))