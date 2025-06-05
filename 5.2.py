for i in range(1000,0,-1):
    a = bin(i)[2:]
    a = [y for y in a]
    if i%2 == 0:
        a[0] = '1'
        a[1] = '0'
        a.append('0')
    else:
        a[0] = '1'
        a[1] = '1'
        a.append('1')
    if int(''.join(a),2) < 35:
        print(i)
        break