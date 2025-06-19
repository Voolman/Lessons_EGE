b = [i for i in range(60,81)]
m = []
for A in range(1,1000):
    for x in range(1000):
        if not((x%A == 0) or ((x in b) <= (not(x%22==0)))):
            break
    else:
        m.append(A)
print(max(m))