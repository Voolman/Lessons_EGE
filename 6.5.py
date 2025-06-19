k = 0
for x in range(1,16):
    for y in range(1,16):
        if (y > x) and (y < (11*2**0.5-x)):
            k+=1
print(k*2)