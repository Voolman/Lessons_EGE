from fnmatch import fnmatch


def f(x):
    s = []
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            s.append(i)
            if x//i != i:
                s.append(x//i)
    if s:
        return sum(s)
    return 0

m = '193*7?'
for y in range(2068,10**9,2068):
    h = f(y)
    if fnmatch(str(y), m) and h % 7 == 0:
        print(y, h)