def f(x):

    s = []
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            s.append(i)
            if x//i != i:
                s.append(x//i)

    if len(s) > 0:
        return int(sum(s)/len(s))
    return 0

d = 0
y = 550001
while d < 5:
    n = f(y)

    if n % 31 == 13:
        print(y, n)
        d += 1
    y += 1