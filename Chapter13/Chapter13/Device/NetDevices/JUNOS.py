#coding: utf-8
from NetDevices.Device import Device
from pexpect import EOF, TIMEOUT


class JUNOS(Device):

    def __init__(self, device):
        super(JUNOS, self).__init__(device)
        self.prompt = self.username + "@" + self.hostname + "[>|#]"

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

