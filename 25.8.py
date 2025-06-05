def f(x):
    s = []
    for i in range(1, x):
        if x%i == 0 and h(i):
            s.append(i)

    return sum(s)
def h(x):
    if x<= 1:
        return False
    if x == 2:
        return True
    if x%2 == 0:
        return False
    for i in range(3, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
k = 0
y = 670001
while k < 5:
    j = f(y)
    if j%10 == 5:
        print(y, j)
        k+=1
    y += 1