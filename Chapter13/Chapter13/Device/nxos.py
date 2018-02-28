from NetDevices import NXOS

nxos1 = {"hostname": "NXOS-1",
             "mgt_ip": "172.20.100.13",
              "username": "admin",
              "password": "Admin@123"}
conn = NXOS(nxos1)
conn.connect()
conn.login()
print(conn.get_config())
