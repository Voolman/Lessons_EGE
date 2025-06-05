s = sorted('СУБЛИМАЦЯ')
k = 0
l = []
for x in s:
    for x1 in s:
        for x2 in s:
            for x3 in s:
                for x4 in s:
                    j = x+x1+x2+x3+x4
                    k += 1
                    if k % 2 == 1 and j[-1] != 'Я':
                        j = j.replace('У', '*').replace('И', '*').replace('А', '*').replace('Я', '*')
                        if j.count('*') == 2:
                            l.append(k)
print(max(l))