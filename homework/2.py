for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((z <= x) and ((not(y) and ((not(w) == y)))))
                h = str(x)+str(y)+str(z)+str(w)
                if h.count('0') >= 1 and y == 1 and f == 0:
                    print(x,y,z,w,f)