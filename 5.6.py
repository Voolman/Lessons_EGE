def f(x):
    s = ''
    while x>0:
        s = str(x%3)+s
        x = x//3
    return s
b = []
for i in range(1,100):
    a = f(i)
    if i%3 == 0:
        a += a[-2:]
    else:
        a += f((i%3)*5)
    if int(a,3)>133:
        b.append(int(a,3))

print(min(b))
