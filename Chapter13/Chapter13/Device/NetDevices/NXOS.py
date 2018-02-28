#coding:utf-8
from NetDevices.Device import Device
from pexpect import EOF,TIMEOUT

class NXOS(Device):

    def __init__(self, device):
        super(NXOS, self).__init__(device)
        self.prompt = self.hostname + "[>|#]\s?"

    def login(self, prompt=""):
        if not prompt:
            prompt = self.prompt
        return super(NXOS, self).login(prompt)

    def _set_terminal_length_zero(self):
        self.c.sendline("terminal length 0")
        try:
            i = self.c.expect(self.prompt)
        except EOF:
            pass
        except TIMEOUT:
            print("session timeout")

    def get_config(self):
        self.expect_list = []
        self.expect_list.append(self.prompt)
        result = []
        self.c.sendline("show running-config")
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
