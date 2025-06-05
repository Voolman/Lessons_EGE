f = open('24.5.txt').readline()

k = 0
s= ''
i = 0
mx = 0
while i < len(f):
    if f[i:i+2] in ['XY', 'ZY']:
        s += f[i:i+2]
        k+=1
        i += 2
    else:
        if 'XYZY' in s:
            mx = max(mx,k-1)
        else:
            mx = max(mx, k)
        s =''
        k = 0
        i += 1
print(mx)