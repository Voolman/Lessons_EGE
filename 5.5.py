for i in range(1000):
    a = bin(i)[2:]
    a = ''.join([y*2 for y in a])
    if int(a,2)>63:
        print(int(a,2))
        break
