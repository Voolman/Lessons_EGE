def f(x):
    s = ''
    while x>0:
        s = str(x%3) + s
        x = x//3
    return s
j = []
for i in range(10000):
    a = f(i)
    b = sum([int(y) for y in a])
    if b%4 == 0:
        a = '1'+a[0:len(a)-2]
    else:
        a += f((b%4)*3)
    if int(a,3)>353:
        j.append(int(a,3))
print(min(j))