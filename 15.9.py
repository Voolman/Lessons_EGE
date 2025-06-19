b = [i for i in range(36,75)]
c = [i for i in range(60,110)]
m = []
for Amin in range(0,111):
    for Amax in range(Amin+1,111):
        A = [i for i in range(Amin,Amax)]
        l = 1
        for x in range(0,111):
            f = (not(x in A)) <= ((x in b) == (x in c))
            if not f:
                l = 0
                break
        if l == 1:
            m.append(Amax-Amin)

print(min(m))