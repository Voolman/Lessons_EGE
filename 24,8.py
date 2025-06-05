a = open('7494.txt').readline()
a = a.replace('DE','*')
b = a.split('*')
k = 0
mx = 0
l = 0
for i in b:
    if k < 241:
        l += len(i) + 2
        k += 1
    else:
        mx = max(mx,l)
        k = 0
        l = 0
print(mx)