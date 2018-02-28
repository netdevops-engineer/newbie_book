#!/usr/bin/env python
#coding: utf-8
import pexpect
from pexpect import EOF, TIMEOUT

def ssh_connect(username, address, port):

    ssh_command = 'ssh  -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -l %s %s -p %d' % (
        username, address, port)
    return pexpect.spawn(ssh_command)


class Device(object):

    def __init__(self, device):

        self.hostname = device.get("hostname")
        self.mgt_ip = device.get("mgt_ip")
        self.username = device.get("username")
        self.password = device.get("password")
        self.port = device.get("port", 22)
        self.expect_list = []

    def connect(self, timeout=30):
        self.c = ssh_connect(self.username, self.mgt_ip, self.port)
        self.c.delaybeforesend = 0.10
        return self.c

    def login(self, prompt=r"[>|#|$]\s?$"):
        self.expect_list = []
        self.expect_list.append(r"(?i)username[:]?$")
        self.expect_list.append(r"(?i)login[:]?$")
        self.expect_list.append(r"(?i)password[:]?$")
        self.expect_list.append(prompt)
        for _ in range(0, 2):
            result = []
            try:
                i = self.c.expect(self.expect_list, timeout=5)
                result.append(i)
                result.append(str(self.c.before))
                result.append(str(self.c.after))
                if i < 2:
                    self.c.sendline(self.username)
                elif i == 2:
                    self.c.sendline(self.password)
                elif i == 3:
                    break                    
            except EOF:
                break
            except TIMEOUT:
                print("connect to %s timeout" %self.hostname)
                break

        if result[0] < 3:
            print("username or password error")
        self.expect_list = []
        return result


    def _set_terminal_length(self):
        pass

    def get_config(self):
        pass

    def logout(self):
        if self.c:
            self.c.terminate()

    def __del__(self):
        self.logout()


class JUNOS(Device):

    def __init__(self,device):
        super(JUNOS, self).__init__(device)
        self.prompt = self.username + "@" + self.hostname + ">"
        
    def login(self, prompt=""):
        if not prompt:
            prompt = self.prompt
        return super(JUNOS, self).login(prompt)
        
    def get_config(self):
        self.expect_list = []
        self.expect_list.append(self.prompt)
        result = []
        self.c.sendline("show config | no-more")
        try:
            i = self.c.expect(self.expect_list, timeout=5)
            if i == 0:
                result.append(i)
                result.append(str(self.c.before))
                result.append(str(self.c.after))
        except EOF:
            pass
        except TIMEOUT:
            print("session timeout")
        return result

if __name__ == "__main__":

    d = {"hostname": "vMX-1",
         "mgt_ip": "172.20.100.11",
         "username": "admin",
         "password": "lab123"}


    conn = JUNOS(d)
    conn.connect()
    r = conn.login()
    print(r)
    print(conn.get_config())
