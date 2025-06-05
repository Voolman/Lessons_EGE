from itertools import *

k = 0
for i in product('0123456789AB', repeat = 5):
    s = ''. join(i)
    s = s.replace('9', '*').replace('A', '*').replace('B','*')

    if s[0] != '0' and s.count('7') == 1 and s.count('*') <= 3:
        k+= 1
print(k)