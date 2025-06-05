from itertools import *

k = 0
for i in product('012345', repeat = 6):
    s = ''.join(i)
    s = s.replace('1','*').replace('3', '*').replace('5','*')
    if s[0] != '0' and s.count('2') == 1 and '*2' not in s and '2*' not in s:
        k += 1
print(k)