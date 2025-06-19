for A in range(0,1000):
    for x in range(1000):
        l = 0
        for y in range(1000):
            if not((5 < y) or (x > 32) or (x+2*y < A)):
                l  = 1
                break
        if l:
            break
    else:
        print(A)
        break