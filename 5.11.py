for i in range(100,1000):
    a = str(i)
    t1,t2,t3 = int(a[0]), int(a[1]), int(a[2])
    c1 = t1**2 + t2**2
    c2 = t2**2 + t3**2
    b = str(max(c1,c2)) + str(min(c1,c2))
    if b == '9010':
        print(i)
        break