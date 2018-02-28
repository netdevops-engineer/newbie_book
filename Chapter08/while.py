#!/usr/bin/python
devices = {"R1": "1.1.1.1",
           "R2": "1.1.1.2",
           "R3": "1.1.1.3",
           "R4": "1.1.1.4"}

while True:
    router_list = devices.keys()
    router_list = sorted(router_list)
    for router_name in router_list:
        print(router_name)

    print("input e to exit ")
    router_input = input("Please select one router: ")
    router_input = router_input.upper()
    if router_input in devices.keys():
        print("I will connect to router %s %s" %(router_input, devices[router_input]))
    elif router_input == "E":
        break
    else:
        print("unknow host")
