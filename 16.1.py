def f(n):
    if n <= 5:
        return n
    if n%5 == 0:
        return n + f(n//5+1)
    return n+f(n+6)

k = 0
for i in range(1,1000):
    try:
        if f(i)>1000:
            print(i)
    except:
        pass