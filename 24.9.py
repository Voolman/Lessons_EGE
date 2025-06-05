a = open('7495.txt').readline() + '**'
k = 0
mx = 0
L = 0
R = 0
while L < len(a):
    while R < len(a)-1 and k < 161:
        if a[R:R+2] == 'CD': k += 1
        if k < 161:
            mx = max(mx,R-L+2)
        R+=1
    while L < len(a)-1 and a[L:L+2] != 'CD':
        L+=1
    k-=1
    L+=1
print(mx)