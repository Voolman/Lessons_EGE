a = open('24.24.3.txt').readline()
i = 0
k = 0
mx = 0
R = 0
while i < len(a):
    while R < len(a) and k < 81:
        if a[R:R+4] == 'FSRQ': k +=1
        if k == 81:
            mx = max(mx, R-i+3)
        R+=1
    while i < len(a)-1 and a[i:i+4] != 'FSRQ':
        i +=1
    k -= 1
    i += 1
print(mx)
