from fnmatch import fnmatch


def f(x):
    s = []
    for i in range(1,int(x**0.5) + 1):
        if x%i == 0:
            s.append(i)
            if x//i != i:
                s.append(x//i)
    if s:
        return s
    return 0

m = '*7?'
for x in range(400000,500001):
    h = [y for y in f(x) if fnmatch(str(y),m)]
    if len(h) >= 18:
        print(x, sum(h))