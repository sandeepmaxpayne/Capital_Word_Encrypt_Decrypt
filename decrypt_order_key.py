''' To find out the order key from encrypted format and return a dictionary of keys c, n and s'''

import re

class OrderKey:
    def __init__(self, encrypted_order_key_input):
        super().__init__()
        self.encrypted_order_key_input = encrypted_order_key_input
    
    def decrypt_order_key(self):
        split_order_values = re.findall(r'\d+', self.encrypted_order_key_input)
        split_order_keys = re.findall(r'\D+', self.encrypted_order_key_input)
        dict_order = dict(zip(split_order_keys, split_order_values))
        # print(f'split_order: {split_order_values}, {split_order_keys}')
        # print(f'dict order: {dict_order}')
        return dict_order