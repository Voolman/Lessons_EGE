from itertools import *

k = 0
for i in permutations('КОБУРА', r=6):
    s = ''.join(i)
    s = s.replace('К', '*').replace('Б', '*').replace('Р', '*')
    s = s.replace('О', '+').replace('У', '+').replace('А', '+')
    if '**' not in s and '++' not in s:
        k += 1
print(k)