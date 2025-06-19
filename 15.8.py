for A in range(0,1000):
    for x in range(0,1000):
        if not(((x&52 != 0) and (x&48 == 0)) <= (not((x&A) == 0))):
            break
    else:
        print(A)
        break