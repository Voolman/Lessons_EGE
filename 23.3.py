import math
def f(a,b):
    if a == b:
        return 1
    if a < b:
        return 0
    if bin(a).count('1') == 1:
        return f(a-1,b)
    else:
        return f(a - 1, b) + f(2 ** int(math.log(a, 2)), b)
print(f(12,4))