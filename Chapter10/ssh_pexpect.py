#coding:utf-8
#!/usr/bin/python
import sys, getpass
import pexpect

def print_lines(outputs):
    for line in outputs.splitlines():
        print(line.decode("utf-8"))

def ssh_login(hostname, username, password, port=22):
    ssh_cmd = "ssh -l %s -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null %s"
    child = pexpect.spawn(ssh_cmd %(username, hostname))
    i = child.expect([pexpect.TIMEOUT, "password:"])
    if i == 0:
        print("Connect timeout")
        print_lines(child.before)
        print_lines(child.after)
        sys.exit(1)
    elif i == 1:
        child.sendline(password)
        if child.expect([pexpect.TIMEOUT, "#"]) == 1:
            return child
        else:
            print("timeout")
            sys.exit(1)

def show_cmd(child, cmd, host_str):
    child.sendline(cmd)
    i = child.expect([pexpect.TIMEOUT, host_str])
    if i == 0:
        print("Connect timeout")
        print_lines(child.before)
        print_lines(child.after)
        sys.exit(1)
    elif i == 1:
        print_lines(child.before)
        print_lines(child.after)
        

if __name__ == '__main__':
    hostname = "172.20.1.10"
    username = "admin"
    host_str = "R2#"
    password = getpass.getpass()

    child = ssh_login(hostname, username, password)
    show_cmd(child, "terminal length 0", host_str)
    show_cmd(child, "show version", host_str)
    show_cmd(child, "show running", host_str)



        



