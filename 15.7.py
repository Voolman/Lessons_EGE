for a in range(1000):
    f = 0
    for x in range(1000):
        for y in range(1000):
            if not(3*x+2*y>95 or 4*x<3*y or x+4*y<a):
                print(a)
                f = 1
                break
        if f:break