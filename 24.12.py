a = open('7497.txt').readline()
mx = 0
for i in range(len(a)):
    if a[i] not in '789':continue
    r = i
    while r < len(a)-2 and a[r:r+2] not in ['--','-*','*-',"**",'-0','*0']:
        r+=1
    mx = max(mx,r-i)
print(mx)