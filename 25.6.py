def f(x):
    k = []
    for i in range(1, x+1):
        if x%i == 0 and i%2==0 :
            k.append(i)
    if len(k) == 4:
        return k
    return []

for y in range(190201,190261):
    n = sorted(f(y))
    if n:
        print(n[3], n[2])