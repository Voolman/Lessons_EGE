for a in range(1,10000):
    for x in range(1,10000):
        if not((x&53 == 0) <= ((x&19 != 0) <= (x&a !=0))):
            break
    else:
        print(a)
        break