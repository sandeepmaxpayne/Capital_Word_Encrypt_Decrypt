''' Continuation of the previous encrypted text for small encrypted'''
''' For decrypting small letters Logic is only for pos0 for each number generated
        1 => 10
        2 => 11
        3 => 12
        Done in decrypt_ascii[]
'''
import re
class DecryptSmallLetter():
    def __init__(self, input_encrypted_small):
        super().__init__()
        self.input_encrypted_small = input_encrypted_small
        self.__decrpt_ascii = []
        self.__decrypt_index1 = '' 
        self.__decrypt_index2 = ''
        self.__decrypted_secret_key_small = 0

    def decrypt_small(self):
       # encrpted_small_text = 'gjd3yssurvurrxvsx'
        encrpted_small_text = self.input_encrypted_small
       # print(encrpted_small_text)
        encryp_x = re.split(r'\d', encrpted_small_text)
       # print(f'smallencyrpt: {encryp_x}')
        ''' Count the number  '''
        iter_count = re.findall(r'\d+', encrpted_small_text)
       # print(f'iter count: {iter_count}')
        ''' Reverse the [index 2] encrypted text'''
        rev_small_encry_x = encryp_x[1][::-1]
        #print(f'reversed index 2: {rev_small_encry_x}') 
    
        ''' Decrypting using manimulation of ascii for small '''
    
        ''' Decrypt the first encrypted index characters'''
        for i in encryp_x[0]:
            start = 97
            start_decrypt = ord(i)
            self.__decrypt_index1 += str(start_decrypt - start)
       # print(f'decrypt_index1: {self.__decrypt_index1}') 

        ''' Decrypt the second encrypted index charcaters in reversed order'''
        for i in rev_small_encry_x:
            last = 122
            rev_decrypt = ord(i)
            self.__decrypt_index2 += str(last - rev_decrypt)
       # print(f'decrptedindex2: {self.__decrypt_index2}')

        '''Form the original decimal value of 127 numbeer system '''
        decrypt_value = float(f'{self.__decrypt_index1}.{self.__decrypt_index2}')
        #print(f'decrypte value: {decrypt_value}, type: {type(decrypt_value)}')
        s1 = 0
        if len(iter_count) > 0:
            for j in range(int(iter_count[0]) - 1):
                s = decrypt_value
                s1 = 127 * s
                decrypt_value = s1
        else:
            '''TODO for iter < 2 if any '''
            s1 = int(decrypt_value)
       # print(f'float value: {s1}')
        decrypt_value = s1
       # print(f'decrypted value: {decrypt_value}, type: {type(decrypt_value)}')
        y = re.findall(r'\d{2}', str(decrypt_value))
       # print(f' list y val: {y}, type[index0]:{type(y[0])}')

        '''Arrange the single digit number of pos0 to 2 digit number '''
        for j in y:
            if j[0].__eq__('1'):
                self.__decrpt_ascii.append(f'10{j[1]}')
            elif j[0].__eq__('2'):
                self.__decrpt_ascii.append(f'11{j[1]}')
            elif j[0].__eq__('3'):
                self.__decrpt_ascii.append(f'12{j[1]}')
            else:
                self.__decrpt_ascii.append(j)
       # print(f'decrpt_ascii: {self.__decrpt_ascii}')
        decrpted_small_txt = ''
        for i in self.__decrpt_ascii:
            decrpted_small_txt += chr(int(i))
        #print(f'decrypted small text: {decrpted_small_txt}')
        ''' calculate the secret key '''
        self.__decrypted_secret_key_small = int(self.__decrypt_index1) ^ int(self.__decrypt_index2)
        return (decrpted_small_txt, self.__decrypted_secret_key_small)