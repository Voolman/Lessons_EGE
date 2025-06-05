def f(x):
    s = ''
    while x > 0:
        s = str(x%7) + s
        x = x//7
    return s

for i in range(1000,0,-1):
    n = f(i)
    if i % 7 == 0:
        n = n + n[-2:]
    else:
        n = n + f(i%7*2)
    if int(n,7) < 220:
        print(i)
        break