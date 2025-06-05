from fnmatch import *
m = '17*023?9'
k = 0
for i in range(10**8,10**10):
    if k == 5:
        break
    g = sum(map(int, str(i)))
    if  g % 11 == 0 and fnmatch(str(i), m):
        print(i,g//11)
        k += 1
