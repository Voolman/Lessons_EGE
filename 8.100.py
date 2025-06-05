k = 0
for i1 in 'воздух':
    for i2 in 'воздух':
        for i3 in 'воздух':
            for i4 in 'воздух':
                for i5 in 'воздух':
                        s = i1+i2+i3+i4+i5
                        if (s.count('о') + s.count('у') == 1) and s.count('ву') + s.count('ув')+ s.count('ов')+ s.count('во') + s.count('ху') + s.count('ух')+ s.count('ох')+ s.count('хо') == 0:
                            k += 1

print(k)