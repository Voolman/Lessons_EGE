def f(a,b,s, d):
    if a == 18: d = 1
    if a > b or s > 5 or a == 11 or a == 35:
        return 0
    if a == b:
        return  d==1
    return f(a+1,b,s+1, d) + f(a+3,b,s, d) + f(a*2,b,s,d)

print(f(2,40,0, 0))