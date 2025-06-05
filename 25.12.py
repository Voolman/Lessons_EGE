from fnmatch import *
from math import *

m='17*46??8'

for i in range(86513,10**12,86513):
    if fnmatch(str(i), m) and int(sum(map(int, str(i)))**0.5)**2 == sum(map(int, str(i))):
        print(i,i//86513)