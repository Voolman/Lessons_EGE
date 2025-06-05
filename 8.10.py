k = 0
s = sorted('СОЛНЦЕ')
for x in s:
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    j = x+x1+x2+x3+x4
                    k += 1
                    if j.count('Е') < 2 and j.count('Л')== 0:
                        print(k)

