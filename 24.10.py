a = open('7495.txt').readline()+'**'
L=0
R=0
k=0
mx=100000000000
while L < len(a):
    while R < len(a)-1 and k < 200:
        if a[R:R+2] == 'AF': k+=1
        if k == 200:
            mx = min(mx,R-L+3)
        R+=1
    while L < len(a)-1 and a[L:L+2] != "AF":
        L+=1
    k-= 1
    L+=1
print(mx)