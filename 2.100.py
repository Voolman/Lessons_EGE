for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f =  (not((y<=w) == x)) and z
                print(x,y,z,w,f)