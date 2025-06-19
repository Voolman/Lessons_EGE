k = 0
for i in open('1.csv'):
    M = [int(x) for x in i.split(';')]
    M.sort()

    if (M[0]+M[-1])**2 > (M[1]**2 + M[2]**2):
        k+=1
print(k)