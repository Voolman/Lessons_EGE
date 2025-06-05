f = open('24.2.txt').readline()
a = ['AB', 'CB']
mx = 0
k = 0
i = 0
while i < len(f):
    if f[i:i+2] in a:
        k += 1
        i+=1
    else:
        mx = max(mx,k)
        k = 0
    i+=1
print(mx)