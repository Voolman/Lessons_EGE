def f(x):
    sr = '0123456789AB'
    s = ''
    while x>0:
        s = sr[x%12] + s
        x = x//12
    return s

for i in range(1000,0,-1):
    a = f(i)
    if i%3 == 0:
        a = '1' + a + 'B'
    else:
        a = '2' + a + '0'
    if int(a,12) < 1996:
        print(int(a,12))
        break
