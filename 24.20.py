a = open('24.24.8.txt').readline()
mx = 0
s = ''
for i in range(len(a)):
    if a[i] in '-*' or a[i:i+2] in ['06','07','08', '09', '--','**','-*','*-']: continue
    r = i
    while r < len(a) and a[r:r+3] not in ['-06','-07','-08','-09','*09','*08',"*07",'*06'] and a[r:r+2] not in ['--','**','-*',"*-"]:
        r += 1
    if a[r:r+3] in ['-06','-07','-08','-09','*09','*08',"*07",'*06']:
        mx =max(mx,r-i+1)
        if len(s) < mx:
            s = a[i:r+2]
    else:
        mx = max(mx, r - i)
        if len(s) < mx:
            s = a[i:r+1]

print(mx)