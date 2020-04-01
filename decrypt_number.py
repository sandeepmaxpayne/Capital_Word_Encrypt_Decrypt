''' For ecrypting the number I used default ascii 78 so for decrypting it here I'll need the same value'''

import re

class Number_decryption:
    def __init__(self, encrypted_number_input):
        self.encrypted_number_input = encrypted_number_input
        self.__get_ascii = ''
        self.__decrypted_ascii = ''
        self.__decrypt_number = ''
        self.__default_num_ascii = 78

    ''' decrypt number function callable '''    
    def decrypt_number_function(self):
        for i in self.encrypted_number_input:
            self.__get_ascii += str(ord(i))
        #print(f'getAscii: {self.get_ascii}')
        split_num_2dig = re.findall(r'\d{2}', self.__get_ascii)
        #print(f'splitascii: {split_num_2dig}')
        for i in split_num_2dig[::-1]:
            self.__decrypted_ascii += str((int(i) - self.__default_num_ascii)) 
        split_decrypt_ascii = re.findall(r'\d{2}', self.__decrypted_ascii)
        #print(f'decrypted ascii: {split_decrypt_ascii}')
        for i in split_decrypt_ascii:
            self.__decrypt_number += chr(int(i))
        #print(f'decrypted number: {self.decrypt_number}')
        return self.__decrypt_number