class Router(object):

    def __init__(self, params={}):
        self.hostname = params.get("hostname", None)
        self.mgmt_ip = params.get("mgmt_ip", None)

    def connect(self):
        print("connect to %s, ip is %s" %(self.hostname, self.mgmt_ip))


class CiscoIOS(Router):

    def __init__(self, params={}):
        super().__init__(params)
        self.vendor = params.get("vendor")

    def goto_enable(self):
        print("goto enable mode")



device_info = {"hostname": "R1",
               "mgmt_ip": "10.1.1.1",
               "vendor": "CiscoIOS"}

device = CiscoIOS(device_info)
print("device.vendor is : ", device.vendor)
device.connect()
device.goto_enable()
