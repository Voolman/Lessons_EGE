f = open('24.4.txt').readline()
a = [0,0,0]
for i in range(len(f)):
    if f[i:i+3] in ['ABA', 'BAB']:
        a.append(a[i]+1)
    else:
        a.append(0)
print(max(a))