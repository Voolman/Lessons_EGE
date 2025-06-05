from itertools import *

k = 0
for i in permutations('01234567', r = 6):
    s = ''.join(i)
    if s[0] != '0':
        if int(s,8)%5 == 0:
            s = s.replace('0','*').replace('2','*').replace('4','*').replace('6','*')
            s = s.replace('1', '+').replace('3', '+').replace('5', '+').replace('7', '+')
            if '++' not in s and '**' not in s:
                k+=1
print(k)