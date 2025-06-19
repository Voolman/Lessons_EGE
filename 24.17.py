a = open('24.24.4.txt').readline()

r = 0

k = 0
mn = 10000000000
s = []
for l in range(len(a)):
    if a[l] == 'Y':
        k = 0
        r = l+1
    if a[l]== 'X':
        k +=1
    while k >= 500:
        s.append(l-r+1)
        if a[r] == 'X':
            k -= 1
        r +=1
print(min(s))

