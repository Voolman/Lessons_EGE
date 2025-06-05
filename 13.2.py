from ipaddress import *

n = ip_interface('98.112.180.225/255.255.240.0')
print(n.network.broadcast_address)