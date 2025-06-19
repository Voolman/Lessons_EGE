def f(x, y, z, k):
    if k == 3 and x+y+z <= 16:
        return 1
    elif k == 3 and x+y+z > 16:
        return 0
    elif k < 3 and x+y+z <= 16:
        return 0
    else:
        if k % 2 == 0:
            return f(x-1,y,z,k+1) or f(round(x/2),y,z,k+1) or f(x,y-1,z,k+1) or f(x,round(y/2),z,k+1) or f(x,y,z-1,k+1) or f(x,y,round(z/2), k+1)
        else:
            return f(x - 1, y, z, k + 1) or f(round(x/2), y, z, k + 1) or f(x, y - 1, z, k + 1) or f(x, round(y/2), z,k + 1) or f(x, y,z - 1,k + 1) or f(x, y, round(z/2), k + 1)

for x in range(1000,16,-1):
    if f(3,4,x,1) == 1:
        print(x)