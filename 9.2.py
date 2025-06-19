k = 0
for i in open('2.csv'):
    m = [int(x) for x in i.split(';')]
    if len(m) == len(set(m)):
        m.sort()
        if m[0]+m[-1] < (sum(m)-m[0]-m[-1])*3/4:
            k+=1
print(k)