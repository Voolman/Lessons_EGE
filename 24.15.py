f = open('24.24.2.txt').readline()

k = 0
i = 0
s = []
while i < len(f):
    if f[i:i+2] in ['RQ','RS','RR','QR','QS','QQ','SR','SQ','SS']:
        k += 1
        s.append(k)
        k = 1
        i += 2
    else:
        k+=1
        i += 1
print(max(s))