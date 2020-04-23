import re
import decryptSmall
import decrypt_number
import decrypt_order_key

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

    complex_encrypted_text = 'GFJG2SXRURWWYQXQT-bbda10wrqqtzttrzvwq-OSNSWR'
    separate_complex = complex_encrypted_text.split('-')
    print(f'compex separated: {separate_complex}')

    # small_encrypted_input = 'gjd3yssurvurrxvsx'
    # number_encrypted_input = 'VR'


    for i in separate_complex:
        if i[0].islower():
            small_encrypted_input  = i
        elif i[0].isupper() and re.findall(r'\d+', i):
            capital_encrp_text = i
        else:
            number_encrypted_input = i
    
    print(f'cap_encypted: {capital_encrp_text}, small_encrypted: {small_encrypted_input}, number_encrypted: {number_encrypted_input}')
  
   
    ErrRed = lambda x: '\033[31m' + str(x)
 
    ''' suppose 10000 is main key do sub and get pub and priv key, then combine both to get exact to get sol'''
    secret_key = 692913383591
   # encrp_text = input("Enter the encrypted text: ")
    # capital_encrp_text = 'DFEJ4UYTYSSQWUSXZ'
    #secret_key = int(input("Enter secret key: "))
    iter = re.findall(r'\d+', capital_encrp_text)
    x = re.split(r'\d+', capital_encrp_text)
    print(f' iteration : {x}, {iter}')

    ''' TODO Decrypt the capital encypted text'''
    #print(iter)
    if len(iter) < 1:
        shortMsg = Decrypt_Single_Message(capital_encrp_text)
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
 

        ''' to decrypt the first index of x list'''
        for i in x[0]:
            start = 65
            start_dec = ord(i)
            decryp1 += str(start_dec - start)

        decryp_val = f'{decryp1}.{decryp2}'
        # print(float(decryp_val))

        value = float(decryp_val)

        if len(decryp2).__eq__(0):
            decryp2 = None

        print(f"d1={decryp1}, d2={(decryp2)}")

        if decryp1 is not None and decryp2 is None:
            exact_key = int(str(decryp1))
        else:
            exact_key = int(str(decryp1)) ^ int(decryp2)

        print(f'exact key: {exact_key}')
        # print(iter)
        if exact_key.__eq__(secret_key):
            print("Secrect Key is Correct")
            print("Decrypting Data.......")
            if iter > 1:
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

    '''TODO Decrypt the small letter encypted text '''

    decrypt_small_text = decryptSmall.DecryptSmallLetter(small_encrypted_input).decrypt_small()
    print(f'decrypted small text: {decrypt_small_text}')

    '''TODO Decrypt the encrypted number  '''

    decrypt_number_str = decrypt_number.Number_decryption(number_encrypted_input).decrypt_number_function()
    print(f'decrypted number:  {decrypt_number_str}')

    '''TODO Arrange the order of all decryoted letter and number using the decrypted order dictionary order : Capital + Num + Small '''
    
    ''' Get the encrypyted order key dictionary '''
    # encrypted_order_key = 'c0123456n11s78910'
    encrypted_order_key = 'c0-7-10-n14-15-16-s1-2-3-4-5-6-8-9-11-12-13'
    decrypted_order_key_dict = decrypt_order_key.OrderKey(encrypted_order_key).decryptOrderKey()
    print(f'decrypted order key dict: {decrypted_order_key_dict}')
    
    cap_order = decrypted_order_key_dict[0]
    num_order = decrypted_order_key_dict[1]
    small_order = decrypted_order_key_dict[2]
    
    cap_order.insert(0, cap_order[0][1:])
    cap_order.pop(1)
    num_order.insert(0, num_order[0][1:])
    num_order.pop(1)
    small_order.insert(0, small_order[0][1:])
    small_order.pop(1)
    
    
    print(f'cap_order: {cap_order[0]}, num_order: {num_order}, small_order: {small_order}')
    order_dictionary = cap_order + num_order + small_order
    print(f'order dictionary: {order_dictionary}')

    decrypted_capital_txt = txt
    print(f'decrypted capital text: {decrypted_capital_txt}, decrypted small text: {decrypt_small_text}, decrypted number: {decrypt_number_str}')
    order_decrypt_word = decrypted_capital_txt + decrypt_number_str + decrypt_small_text
    print(f'ordered decrypted word: {order_decrypt_word}')

    
    ''' Get the arranged Dictionary '''
    arr_decrypt_dict = dict(zip(order_dictionary, order_decrypt_word))
    print(f'dict: {arr_decrypt_dict}')
    

    '''Get the decrypted text '''
    print(len(arr_decrypt_dict))
    decrypted_text = ''
    for key in range(len(arr_decrypt_dict)):
        if key.__eq__(arr_decrypt_dict[f'{key}']):
            decrypted_text += arr_decrypt_dict[f'{key}']
    print(f'Decrypted Text: {decrypted_text}')  

   
    

decryptText()