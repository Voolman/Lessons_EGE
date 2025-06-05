k = 0
for x in range(1,13):
    for y in range(1,15):
        if y > (x / 3**0.5) and y < (15 - (x/3**0.5)):
            k+=1
print(k)