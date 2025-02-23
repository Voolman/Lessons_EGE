from fnmatch import *
def f(x):
    d = 2
    while d*d <= x:
        if x % d == 0: return False
        d += 1
    return True
m = '?*23*21'

for x in range((int((10**9)**0.25)+1), (int((10**10)**0.25))):
    if fnmatch(str(x**4),m) and f(x):
        print(x**4, x**2)