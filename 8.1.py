from itertools import *
s = ['К','А','Л','И','Й']
l = 0
for i in permutations('КАЛИЙ', r=5):
    j = ''.join(i)
    if j[0] != 'Й' and j.count('ИА') == 0:
        l += 1
print(l)