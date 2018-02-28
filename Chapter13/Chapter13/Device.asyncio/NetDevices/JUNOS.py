#coding: utf-8
from NetDevices.Device import Device
from pexpect import EOF, TIMEOUT


class JUNOS(Device):

    def __init__(self, device):
        super(JUNOS, self).__init__(device)
        self.prompt = self.username + "@" + self.hostname + "[>|#]"

    async def login(self, prompt=""):
        if not prompt:
            prompt = self.prompt
        await super(JUNOS, self).login(prompt)

    async def get_config(self):
        self.expect_list = []
        self.expect_list.append(self.prompt)
        result = []
        self.c.sendline("show config | no-more")
        try:
            i = await self.c.expect(self.expect_list, timeout=20, async_=True)
            if i == 0:
                result.append(i)
                result.append((self.c.before + self.c.after).decode())
        except EOF:
            pass
        except TIMEOUT:
            print("session timeout")
        return result

