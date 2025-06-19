a = open('24.24.5.txt').readline()

l = 0
r = 0
k = 0
mn = 1000000000

while l < len(a):
    while r < len(a) and k < 130:
        if a[r:r+3] == 'RSQ': k +=1
        if k == 130 and a[l:r+4][-1] != 'Q':
            print(a[r:r+4])
            mn = min(mn,r-l+2)
        if k > 130:
            break
        r +=1
    while l < len(a) and a[l:l+3] != 'RSQ':
        l +=1
    l +=1
    k -=1
print(mn)
