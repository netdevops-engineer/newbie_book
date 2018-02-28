#!/usr/bin/python

def connect(hostname, username="admin", password="admin123", port=23):
    print("connect to %s ...port %d" %(hostname,port))
    print("username is %s" %username)
    print("password is %s" %password)


connect(hostname="r1",username="netdevops")

connect(["r2", "net_admin", "net_admin", 22])

connect(*["r2", "net_admin", "net_admin", 22])

connect(**{"hostname":"r3", "port": 2202, "username":"net_ops"})

#connect(**{"hostname":"r4", "proto": "http", "port":80, "username":"netdevops", "password":"admin"})

def connect_new(hostname, username, password, port, *args, **kwargs):
    print("connect to %s ...port %d" %(hostname,port))
    print("username is %s" %username)
    print("password is %s" %password)
    print("args: ", args)
    print("kwargs: ", kwargs)

connect_new("r4","netdevops","admin",2200,"tcp",site="sha")
