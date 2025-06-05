a = open('24_22235 (1).txt').readline()+"**"
mx = 0
for L in range(len(a)):
    if a[L] not in '0123456789': continue
    R = L
    while R < len(a)-1 and a[R:R+2] not in ['++','+*','*+','**','01','02','03','04','05','06','07','08','09','00']:
        R+=1

    b = a[L:R].replace('+','*').split('*')

    if len(b) == len([i for i in b[0:len(b)-1] if int(i)%2 == 0 or i[-1] == '5']):
        try:
            if eval(a[L:R+1]) == 0:
                mx = max(mx, R-L+1)
        except:
            pass
print(mx)