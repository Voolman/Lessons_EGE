for i in range(1000,0,-1):
    a = bin(i)[2:]
    a = a + str(sum([int(y) for y in a])%2)
    a = a + str(sum([int(y) for y in a])%2)
    if int(a,2) < 86:
        print(i)
        break