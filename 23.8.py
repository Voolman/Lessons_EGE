def f(a,b, s):
    if a > b or s.count('AAA') > 0:
        return 0
    if a == b:
        return 1
    return f(a-1,b, s+'A') + f(a+5,b,s+'B') + f(a*2,b,s+'C')
print(f(5,34, ''))