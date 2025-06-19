for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z and (not(w or x)) or (not(z or y)) and (not w))
                if f:
                    print(x,y,z,w)