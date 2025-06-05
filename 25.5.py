def f(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return i + x//i
    return 0

k = 0
y = 452022
while k < 5:
    n = f(y)
    
    if n % 7 == 3:
        k += 1
        print(y, n)
    y += 1