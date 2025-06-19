def f(x):
    s = []
    for i in range(1,int(x**0.5)+1):
        if x%i == 0 and g(i):
            s.append(i)
            break
    for i in range(x,1,-1):
        if x%i == 0 and g(i):
            s.append(i)
            break
    return max(s) + min(s) if s else 0

def g(r):
    if r <= 1:
        return False
    if r == 2:
        return  True
    if r%2 == 0:
        return False
    for a in range(3,int(r**0.5)+1):
        if r%a == 0:
            return False
    return True

k = 0
y = 23600001
while k < 5:
    h = f(y)
    if h % 213 == 171:
        print(y,h)
        k += 1
    y += 1