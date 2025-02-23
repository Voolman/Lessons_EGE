from fnmatch import *
m = '1?1?1?1*1'
for x in range(2023, 10**10,2023):
    if fnmatch(str(x),m) and sum(map(int, str(x))) ==  22:
        print(x, x//2023)