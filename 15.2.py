for a in range(1,10000):
    for x in range(1,1000):
        if not((x%a!=0) <= ((x%6==0) <= (x%9!=0))):
            break
    else:
        print(a)