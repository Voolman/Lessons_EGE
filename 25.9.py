def f(x):
    for i in range(9,x,10):
        if x%i == 0 and i != 9:
            return i
    return 0

k = 0
y = 800001
while k < 5:
    h = f(y)
    if h != 0:
        print(y,h)
        k += 1
    y += 1