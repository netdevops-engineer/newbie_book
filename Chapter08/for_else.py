#!/usr/bin/python
ip_list = ["10.1.1.1", "10.1.1.2", "10.1.1.3", "10.1.1.4"]

IP = input("Please input ip address: ")

for ip in ip_list:
    if ip == IP:
        print("IP address: %s  be found in the ip list" % IP)
        break
else:
    print("Can't find the IP address: %s in the ip list" %IP)
