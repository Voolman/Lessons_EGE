for i in range(1000,10000):
    a = str(i)
    t1, t2, t3, t4 = int(a[0]), int(a[1]), int(a[2]), int(a[3])
    c1 = t1*t2
    c2 = t1*t3
    c3 = t1*t4
    b2 = []
    b2.append(c1)
    b2.append(c2)
    b2.append(c3)

    b2 = sorted(b2)
    n = str(b2[1]) + str(b2[2])
    if n == '5472':
        print(i)
        break