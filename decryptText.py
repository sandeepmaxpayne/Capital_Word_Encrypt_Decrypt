import re
import decryptSmall
import decrypt_number

class Decrypt_Single_Message:
    def __init__(self, encypt_Text):
        self.encrypt_text = encypt_Text
    def decrpt_message(self):
        if int(ord(self.encrypt_text)).__eq__(65):
            self.encrypt_text = chr(90)
        else:
            self.encrypt_text = chr(ord(self.encrypt_text) - 1)
        return self.encrypt_text


def number_system_127(decimal_number):
    pass

def decryptText():
    '''TODO input of encrypted text '''

    complex_encrypted_text = 'DFEJ4UYTYSSQWUSXZ-gjd3yssurvurrxvsx-QSPSOSNSWR'
    separate_complex = complex_encrypted_text.split('-')
    print(f'compex separated: {separate_complex}')

    small_encrypted_input = 'gjd3yssurvurrxvsx'
    number_encrypted_input = 'VR'
    encrypted_order_key = 'c0n5s1234'

    # ss = decryptSmall.DecryptSmallLetter(small_encrypted_input)
    # print(f'decrypted small: {ss.decrypt_small()}')

    # s = decrypt_number.Number_decryption('QSPSOSNSWR')
    # print(s.decrypt_number_function())
   
    ErrRed = lambda x: '\033[31m' + str(x)
 
    ''' suppose 10000 is main key do sub and get pub and priv key, then combine both to get exact to get sol'''
    secret_key = 27539741305
   # encrp_text = input("Enter the encrypted text: ")
    encrp_text = 'DFEJ4UYTYSSQWUSXZ'
    #secret_key = int(input("Enter secret key: "))
    iter = re.findall(r'\d', encrp_text)
    x = re.split(r'\d', encrp_text)
    print(x, iter)

    #print(iter)
    if len(iter) < 1:
        shortMsg = Decrypt_Single_Message(encrp_text)
        decrypt_txt = shortMsg.decrpt_message()
        if secret_key.__eq__(0):
            print("Secrect Key is Correct")
            print("Decrypting Data.......")
            print("Decrypted Character: {}".format(decrypt_txt))
        else:
            print(ErrRed("Invalid secret key value entered !"))

    else:
        iter = int(iter[0])

        ''' To reverse the encrypted string after decimal part'''
        x2 = x[1][::-1]
        decryp1, decryp2 = "", ""
        for i in x2:
            last = 90
            rev_dec = 90 - ord(i)
            decryp2 += str(rev_dec)
        #   print(decryp2)

        ''' to decrypt the first index of x list'''
        for i in x[0]:
            start = 65
            start_dec = ord(i)
            decryp1 += str(start_dec - start)
        # print(decryp1)


        decryp_val = f'{decryp1}.{decryp2}'
        # print(float(decryp_val))

        value = float(decryp_val)

        if len(decryp2).__eq__(0):
            decryp2 = None

        # print(f"d1={decryp1}, d2={(decryp2)}")


        if decryp1 is not None and decryp2 is None:
            exact_key = int(str(decryp1) + str(iter))
        else:
            exact_key = int(str(decryp1) + str(iter)) ^ int(decryp2)


        # print(exact_key)
        # print(iter)
        if exact_key.__eq__(secret_key):
            print("Secrect Key is Correct")
            print("Decrypting Data.......")
            if iter > 2:
                for j in range(iter-1):
                    s = value
                    s1 = 127 * s
                    value = s1
            else:
                s1 = value


            # print(s1)
            # print(type(s1))
            value = int(s1)
            print(f'value: {value}')
            y = re.findall(r'\d{2}', str(value))
            print(f'y: {y}')

            txt = ""
            for k in y:
                txt += chr(int(k))
            print("decrpted text: ", txt)

        else:

            print(ErrRed("Invalid secret key cannot be decrypted!!!"))

#76798669

decryptText()