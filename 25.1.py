from fnmatch import *
m = '3?1*57'
for x in range(2023,10**8, 2023):
    if fnmatch(str(x),m):
        print(x,x//2023)