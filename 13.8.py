from ipaddress import *

n = ip_interface('112.208.0.0/255.255.128.0')

k = 0
for i in n.network:
    if bin(int(i))[2:].count('1') % 7 == 0:
        k += 1
print(k)