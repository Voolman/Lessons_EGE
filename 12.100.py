for n in range(1000):
    a = '8'+'5'*n
    while '8858' in a or '555' in a:
        if '8858' in a:
            a = a.replace('8858','4',1)
        else:
            a = a.replace('555', '58', 1)
        if '5858' in a:
            a = a.replace('5858','85',1)
    if sum([int(i) for i in a]) == 66:
        print(n)
        break
