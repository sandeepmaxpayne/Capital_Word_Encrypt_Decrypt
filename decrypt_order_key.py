''' To find out the order key from encrypted format and return a dictionary of keys c, n and s'''


class OrderKey:
    def __init__(self, encrypted_order_key_input):
        super().__init__()
        self.encrypted_order_key_input = encrypted_order_key_input
        self.small = []
        self.cap = []
        self.num = []
        self.token = 0

    def decryptOrderKey(self):
        for i in self.encrypted_order_key_input.strip('-').split('-'):
            if i[0] == 'c':
                self.token = 1
            elif i[0] == 'n':
                self.token = 2
            elif i[0] == 's':
                self.token = 3
            print(i, self.token)
            if self.token == 1:
                self.cap.append(i)
            elif self.token == 2:
                self.num.append(i)
            elif self.token == 3:
                self.small.append(i)
        return((self.cap, self.num, self.small))
