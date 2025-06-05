from fnmatch import *

m = '1*2??76'
for i in range(1923,10**8,1923):
    if fnmatch(str(i), m):
        print(i, i//1923)