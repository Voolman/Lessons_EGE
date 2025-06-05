from ipaddress import *

n = ip_interface('135.13.142.29/255.255.255.128')
print(n.network.broadcast_address)