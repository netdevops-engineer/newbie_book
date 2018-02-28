# coding:utf-8
import sys
import getopt, getpass
from netmiko import ConnectHandler

def usage():
    print("Usage: %s [options] " %sys.argv[0])
    print("-H    : Hostname")
    print("-u    : Username")
    print("-p    : Port default is 22")
    print("-h    : Help informations")

def handler_opts():
    cisco_xrv = {
    'device_type': 'cisco_xr',
    "port": 22
    }

    try:
        opts, args = getopt.getopt(sys.argv[1:], "H:p:u:h", ["hostname", "port", "username","help"])

        if len(sys.argv) == 1:
            usage()
            sys.exit(1)
        port = 0
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit(1)
            elif opt in ("-H", "--hostname"):
                cisco_xrv["ip"] = arg
            elif opt in ("-u", "--username"):
                cisco_xrv["username"] = arg
            elif opt in ("-p", "--port"):
                cisco_xrv["port"] = int(arg)
    except getopt.GetoptError:
        usage()
        sys.exit(1)
    return cisco_xrv


if __name__ == '__main__':
    device = handler_opts()
    device["password"] = getpass.getpass()
    net_connect = ConnectHandler(**device)
    stdout = net_connect.send_command("show ipv4 interface brief")
    print(stdout)

    config_commands = ["interface GigabitEthernet0/0/0/0", "ipv4 address 10.1.1.1/24","no shutdown", "commit"]

    stdout = net_connect.send_config_set(config_commands)
    print(stdout)

    net_connect.exit_config_mode()
    stdout = net_connect.send_command("show ipv4 interface brief")
    print(stdout)