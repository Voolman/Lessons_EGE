for a in range(100, -1, -1):
    f=0
    for x in range(0,100):
        for y in range(0,100):
            if not(3*x + 2*y > 25 or x > 2*y or x+4*y<a):
                print(a)
                f =1
                break
        if f: break

