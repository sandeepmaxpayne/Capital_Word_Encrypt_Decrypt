import re
import os
import sys
import time

script_path = "calculate_decrypt/"

sys.path.append(os.path.abspath(script_path))

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

def decryptText(encrypted_text, secret_keys, encrypted_order):
    '''TODO input of encrypted text '''

    '''Find out the decrypted secret key'''
    decrypted_secret_key_small = 0
    decrypted_secret_key_capital = 0
    decrypted_secret_key_number = 0

   # complex_encrypted_text = 'GJAF2QTTUVTVWRXXW-gii4vrwstxutrsvxq-PSOSNSWR'
   # secret_key = 8942243274196
    complex_encrypted_text = encrypted_text
    secret_key = secret_keys
    separate_complex = complex_encrypted_text.split('-')
   # print(f'compex separated: {separate_complex}')

    # small_encrypted_input = 'gjd3yssurvurrxvsx'
    # number_encrypted_input = 'VR'

    ''' Set the flag=True for single encrypted text and false for combination of 3 (small, capital, number)'''
    flag = False
    if len(separate_complex) == 1:
        flag = True
    elif len(separate_complex) == 3:
        flag = False
    else:
        print("Encrypted in wrong format . Can't decode")
        return
    
    print(f"flag status: {flag}")

    countsmall, countcapital = 0, 0
    if not flag:
        for i in separate_complex:
            if i[0].islower():
                small_encrypted_input  = i
            elif i[0].isupper() and re.findall(r'\d+', i):
                capital_encrp_text = i
            else:
                number_encrypted_input = i
    else:
        for i in separate_complex[0]:
            if i.islower():
                countsmall += 1
            elif i.isupper():
                countcapital += 1

        if countsmall.__eq__(len(separate_complex[0]) - 1):
            small_encrypted_input = separate_complex[0]
            capital_encrp_text = ""
            number_encrypted_input = ""
        elif countcapital.__eq__(len(separate_complex[0]) - 1):
            capital_encrp_text = separate_complex[0]
            small_encrypted_input = ""
            number_encrypted_input = ""
        elif countcapital.__eq__(len(separate_complex[0])):
            number_encrypted_input = separate_complex[0]
            small_encrypted_input = ""
            capital_encrp_text = ""
        
       # print(f'cap_encypted: {capital_encrp_text}, small_encrypted: {small_encrypted_input}, number_encrypted: {number_encrypted_input}')
  
   
    ErrRed = lambda x: '\033[31m' + str(x)
 
    
   # encrp_text = input("Enter the encrypted text: ")
    # capital_encrp_text = 'DFEJ4UYTYSSQWUSXZ'
    #secret_key = int(input("Enter secret key: "))
    txt = ""
    if len(capital_encrp_text) > 0:
        iter = re.findall(r'\d+', capital_encrp_text)
        x = re.split(r'\d+', capital_encrp_text)
       # print(f' iteration : {x}, {iter}')

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
            decrypted_secret_key_capital = exact_key
           
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
           # print(f'value: {value}')
            y = re.findall(r'\d{2}', str(value))
           # print(f'y: {y}')

            for k in y:
                txt += chr(int(k))

            if exact_key.__eq__(secret_key):
                print("Secrect Key is Correct")
                print("Decrypting Data.......")
                time.sleep(0.5)
               
                print("decrpted text: ", txt)

            else:

                print("Invalid secret key cannot be decrypted!!!")

    '''TODO Decrypt the small letter encypted text '''
    if len(small_encrypted_input) > 0:
        decrypt_small_text = decryptSmall.DecryptSmallLetter(small_encrypted_input).decrypt_small()
        decrypted_secret_key_small = decrypt_small_text[1]
        if decrypt_small_text[1].__eq__(secret_key):
            print('Secret key is correct')
            print('Decrypting small text ....')
            time.sleep(0.5)
            print(f'decrypted small text: {decrypt_small_text[0]}')
        else:
            print("Sorry incorrect secret key entered")

    '''TODO Decrypt the encrypted number  '''
    if len(number_encrypted_input) > 0:
        decrypt_number_str = decrypt_number.Number_decryption(number_encrypted_input).decrypt_number_function()
        decrypted_secret_key_number = decrypt_number_str[1]
        if decrypt_number_str[1].__eq__(secret_key):
            print("Secret Key is correct")
            print("Decrypting number .......")
            time.sleep(0.5)
            print(f'decrypted number:  {decrypt_number_str[0]}')
        else:
            print("Incorrect Secret key.")
            print("Access Denied")
    '''TODO Arrange the order of all decryoted letter and number using the decrypted order dictionary order : Capital + Num + Small '''
    
    if not flag:
        ''' Get the encrypyted order key dictionary '''
        # encrypted_order_key_mapping = 'c0-1-2-n6-7-8-9-s3-4-5-10-11-'
        encrypted_order_key_mapping = encrypted_order
        encrypted_order_key = encrypted_order_key_mapping
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
    
    
      #  print(f'cap_order: {cap_order[0]}, num_order: {num_order}, small_order: {small_order}')
        order_dictionary = cap_order + num_order + small_order
       # print(f'order dictionary: {order_dictionary}')

        decrypted_capital_txt = txt
       # print(f'decrypted capital text: {decrypted_capital_txt}, decrypted small text: {decrypt_small_text}, decrypted number: {decrypt_number_str}')
        order_decrypt_word = decrypted_capital_txt + decrypt_number_str[0] + decrypt_small_text[0]
       # print(f'ordered decrypted word: {order_decrypt_word}')

    
        ''' Get the arranged Dictionary '''
        arr_decrypt_dict = dict(zip(order_dictionary, order_decrypt_word))
        print(f'dict: {arr_decrypt_dict}')
    

        '''Calculate the combined decrypted secret key '''
        decrypted_combined_key = decrypted_secret_key_capital ^ decrypted_secret_key_number ^ decrypted_secret_key_small
        print(f"decrypted combined key: {decrypted_combined_key}")

        '''Get the decrypted text '''
        print(len(arr_decrypt_dict))
        decrypted_text = ''
        for key in range(len(arr_decrypt_dict)):
            if key.__eq__(arr_decrypt_dict[f'{key}']):
                decrypted_text += arr_decrypt_dict[f'{key}']

        ''' Compare the combined secret key if matches then get the result otherwise none '''
        if secret_key.__eq__(decrypted_combined_key):
            print('secret key is correct')
            print('fething the decrypted text ....')
            print(f'Decrypted Text: {decrypted_text}')

            return decrypted_text
        else:
            print(ErrRed('incorrect combined secret key.'))
            return "Incorrect combined key"  
    
    else: 
        if countsmall.__eq__(len(separate_complex[0]) - 1):
            return decrypt_small_text[0]
        elif countcapital.__eq__(len(separate_complex[0]) - 1):
            return txt
        elif countcapital.__eq__(len(separate_complex[0])):
            return decrypt_number_str[0]


   
    

#decryptText()