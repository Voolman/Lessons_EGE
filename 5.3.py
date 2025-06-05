for x in range(1000):
    a = bin(x)[2:]
    if x % 5 == 0:
        a += a[-3:]
    else:
        a = bin((x%5)*5) + a
    if int(a,2) > 512:
        print(x)
        break
