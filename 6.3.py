k= 0
for x in range(1,7):
    for y in range(1,17):
        if x < 6 and y > x*3**0.5 and y < (x*3**0.5)+6:
            k+=1
print(k)