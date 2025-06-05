from ipaddress import *

n = ip_interface('136.36.240.16/255.255.255.248')
k= 0

for i in n.network:
    if bin(int(i))[2:].count('101') == 0:
        k += 1

print(k)