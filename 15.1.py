for a in range(1,1000):
    for x in range(1,1000):
        if not((x%a != 0) <= (not((x%21==0)) and not((x%35==0)))):
            break
    else:
        print(a)