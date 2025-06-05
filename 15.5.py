for a in range(1,1000):
    f = 0
    for x in range(1,1000):
        for y in range(1,1000):
            if not(x - 3*y < a or y > 400 or x > 56):
                f = 1
                break
        if f: break
    else:
        print(a)
        break
