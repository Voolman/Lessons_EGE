for n in range(4,9999):
    a = '1'+'9'*n
    while '19' in a or '399' in a or '999' in a:
        if '19' in a:
            a = a.replace('19','9',1)
        if '399' in a:
            a = a.replace('399','91',1)
        if '999' in a:
            a = a.replace('999','3',1)
    if sum([int(x) for x in a]) == 33:
        print(n)
        break