for i in range(2,1000):
    a = bin(i)[2:]
    if len(a)%2 == 0:
        a = a[0:len(a)//2] + '111' + a[len(a)//2:]
    else:
        a = [y for y in a]
        a[0] = '1'
        a[1] = '1'
        a.append('1')
        a = ''.join(a)
    if int(a,2) > 4000:
        print(i)
        break