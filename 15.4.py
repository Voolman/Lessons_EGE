for a in range(10000):
    for x in range(10000):
        if not((((x&112 != 0) or (x&86 != 0)) <= ((x&65 ==0) <= (x&a != 0)))):
            break
    else:
        print(a)
        break