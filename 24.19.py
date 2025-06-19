a = open('24.24.6.txt').readline()+'**'

s = 0
n = 0
for i in range(len(a)):
    if a[i] not in '123456789AB':continue
    r = i+1
    while r < len(a)-1 and a[r] in '0123456789AB':
        l = int(a[i:r], 12)
        if  l % 2 == 1 and l > s:
            s = l
            n = i
        r +=1
print(n)