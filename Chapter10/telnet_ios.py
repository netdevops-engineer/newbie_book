#! encoding:utf-8
import telnetlib


def login(hostname, username, password, port=23):
    
    tn = telnetlib.Telnet(hostname, port=23, timeout=10)
    tn.set_debuglevel(2)
    #输入用户名
    tn.read_until('Username:')
    tn.write(username + "\n")

    #输入登录密码
    tn.read_until("Password:")
    tn.write(password + "\n")

    return tn

if __name__ == "__main__":
    hostname = "172.20.1.100"
    username = "cisco"
    password = "cisco123"

    t = login(hostname, username, password)
    t.read_until("Router#")
    t.write("terminal length 0" + "\n")
    t.read_until("Router#")
    t.write("show version" + "\n")
    t.read_until("Router#")
    t.close()
