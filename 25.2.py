def f(x):
    d = 2
    while d*d <= x:
        if x % d == 0:
            return d + x//d
        d += 1
    return 0
k = 0
x = 800001
while k < 5:
    if f(x) %10 == 4:
        print(x, f(x))
        k += 1
    x += 1