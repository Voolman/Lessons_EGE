k = 0
a = '*'*200
while '****' in a or '???' in a:
    if '****' in a:
        a = a.replace('****','???', 1)
        k+=3
    a = a.replace('??','*', 1)
print(k)