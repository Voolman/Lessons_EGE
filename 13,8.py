from ipaddress import *
k = 0
n = ip_interface('123.222.111.192/255.255.255.248').network
for i in n:
    b = str(i).split('.')[3]
    if bin(int(b))[2:].count('1') % 3 != 0:
        k += 1
print(k)









