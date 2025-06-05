k = 0
for x in '124568':
    for x1 in '012345678':
        for x2 in '012345678':
            for x3 in '012345678':
                for x4 in '012345678':
                    for x5 in '012345678':
                        for x6 in '012345678':
                            s = x+x1+x2+x3+x4+x5+x6
                            if s.count('00') == 0 and s.count('11') == 0 and s.count('22') == 0 and s.count('33') == 0 and s.count('44') == 0 and s.count('55') == 0 and s.count('66') == 0 and s.count('77') == 0 and s.count('88') == 0:
                                k += 1
print(k)