s = sorted('АКЛМНЯ')
k = 0
l = []
for x in s:
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    j = x+x1+x2+x3+x4
                    k += 1
                    if j[0:2] == 'МН':
                        l.append(k)

print(l[-1]-l[0]-1)
