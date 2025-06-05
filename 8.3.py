from itertools import *

k = 0
for i in permutations('АПЕЛЬСИН',r=7):
    s = ''.join(i)
    s = s.replace('П', '*').replace('Л', '*').replace('С', '*').replace('Н', '*')
    if s.count('*Ь*') == s.count('Ь'):
        k += 1
print(k)
