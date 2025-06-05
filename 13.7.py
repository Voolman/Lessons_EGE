from ipaddress import *

n= ip_interface('172.16.160.0/255.255.240.0')
k = 0

for i in n.network:
    if bin(int(i))[2:].count('1')%3 != 0:
        k+=1
print(k)