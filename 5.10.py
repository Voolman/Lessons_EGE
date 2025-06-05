def f(x):
    s = ''
    while x>0:
        s = str(x%4) + s
        x=  x//4
    return s
b = []
for i in range(1,1000,2):
    a = f(i)
    a = [y for y in a]
    if i % 3 == 0:
        print(a)
        c1 = a[0]
        c2 = a[-1]
        a[0] = c2
        a[-1] = c1
        a.append('1')
        print(a)
    else:
        a.append(str(i%3))
    if int(''.join(a),4) < 340:
        b.append(int(''.join(a),4))
print(max(b))
