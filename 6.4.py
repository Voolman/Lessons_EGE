k = 0
for x in range(1,5):
    for y in range(1,8):
        if x < 2.5*3**0.5 and y > x/3**0.5 and  y < x/3**0.5+5:
            k+=1
print(k)