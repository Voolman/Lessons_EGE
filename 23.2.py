def f(a,b):
    if b == 13:
        lst.append(a)
        return
    f(a+3,b+1)
    f(2*a+1, b+1)
lst = []
f(2,0)
print(len(set(lst)))