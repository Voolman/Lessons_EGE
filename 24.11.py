a = open('6676.txt').readline()
k = 0
L = 0
mx = 0
for i in range(len(a)):
    if a[i] not in '123456789ABCDEF': continue
    R = i
    while a[R] in '0123456789ABCDEF':
        R += 1
    mx = max(mx,R-i)
print(mx)
