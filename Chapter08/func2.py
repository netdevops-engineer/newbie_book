#!/usr/bin/python
def ipv4_to_int(ipv4):
    ipv4 = [int(x) for x in ipv4.split(".")]
    ipv4_int = (ipv4[0] << 24) + (ipv4[1] << 16) + (ipv4[2] << 8) + ipv4[3]
    return ipv4_int

def int_to_ipv4(ip_int):
    ipv4 = []
    for x in (24, 16, 8 ,0):
        ipv4.append(str(ip_int >> x & 0xFF))
    return ".".join(ipv4) 


start_ip = "10.1.1.253"

for x in range(0,4):
    ip_address = ipv4_to_int(start_ip) + x * 4
    ip_address = int_to_ipv4(ip_address)
    print("interface gigaEthernet0/1/%d" %x)
    print("  ip address %s 255.255.255.252" %ip_address)
    print("  no shutdown")
    
