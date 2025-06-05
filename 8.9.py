from itertools import *

k = 0
for i in permutations('ПАРИЖАНКА'):
    s = ''.join(i)
    s = s.replace('А', '*').replace('И', '*')
    if s.count('**') == 1 and '***' not in s:
        k += 1
print(k)