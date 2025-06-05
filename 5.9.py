for x in range(1000,0,-1):
    a = oct(x)[2:]
    if x%2 == 0:
        a += str(max([int(y) for y in a]))
    else:
        a += oct(min([int(y) for y in a])*2)[2:]
    if int(a,8) < 313:
        print(x)
        break