k = 0
def f(x):
    j = 0
    for y in x:
        if x.count(y) == 2:
            j += 1
    if j == 4:
        return True
    else:
        return False
for i in open('6.csv'):
    m = [int(x) for x in i.split(';')]
    s = set(m)
    if len(s) == 5 and f(m) and m.count(max(m)) == 1:
        print(m, set(m))
        k+=sum(m)
        break
print(k)