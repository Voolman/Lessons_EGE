k = 0
for x in range(1,6):
    for y in range(1,17):
        if x < 4 * 2**0.5 and y > x and y < x+11:
            k+=1
print(k)