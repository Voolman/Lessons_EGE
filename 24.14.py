f = open('24.24.1.txt').readline()

k = 0
i = 0
s = []
while i < len(f):
    if f[i:i+2] in ['CA','CO','BA','BO','DA','DO']:
        k+=1
        i+=2
    else:
        s.append(k)
        k = 0
        i+=1
print(max(s))