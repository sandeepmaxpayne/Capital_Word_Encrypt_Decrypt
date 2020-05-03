import math
import os
import sys
from termcolor import colored

scriptpath = "calculate_encrypt/"

sys.path.append(os.path.abspath(scriptpath))

from calculate_encrypt import small_letters
from calculate_encrypt import number


'''
    Limitations 
    Only Capitals Words, or ,
    Only Small Words, or ,
    Only Numbers, or ,
    Must be a combination of capital word, small word and numbers
    For secret key get the individual secret key for the encrypted capitals, smalls, numbers 
    For the combination of capital, small and number first get each of their individual sceret key
    and finally the xor each of the individual keys
 '''


class Short_Message:
    def __init__(self, message):
        self.message = message
    def encrypt_single_msg(self):
        if int(ord(self.message)).__eq__(90):
            self.message = chr(65)
        else:
            self.message = chr(ord(self.message) + 1)
        return self.message

def number_system_127(number_value):
   
    c, bb1 = 0, 0
    s = ""
    while round(number_value) > 127:
        r = number_value % 127
        s = s + str(round(r))
        c += 1
        bb1 = number_value
        number_value = number_value / 127
    #print(r, c, bb1, s)
   # print(f'count: {c}')
    strbb1 = str(bb1)
    strbb1 = strbb1.split(".")
    #print(strbb1)
    ''' Add the counter at end of index0'''
    strbb1[0] += "-" + str(c)
   # print(f'function strbb1: {strbb1}')
    ''' return [(Integer Value index1 + counter value), Integer Value index2] '''
    return strbb1
   


def encryptStr(input_msg):

    '''Initialize all the secret keys '''
    secret_key_capital = 0
    secret_key_small = 0
    secret_key_num = 0

    
    # msg = input('enter message: ')
    msg = input_msg

    ''' Check if the input word is Neither only capital nor only small nor only number then go further else go for single checking'''
    flag = False # use to check only num, only small char, only cap if flag = True
    cp, sm, nu = 0, 0, 0
    for i in msg:
        if i.islower():
            sm += 1
        elif i.isupper():
            cp += 1
        elif i.isdigit():
            nu += 1
   # print(f'count cap: {cp}, count small: {sm}, count number: {nu}')

    if len(msg).__eq__(cp):
        flag = True
    elif len(msg).__eq__(sm):
        flag = True
    elif len(msg).__eq__(nu):
        flag = True
    else:
        flag = False



    ''' Use Dict to get the records of small letters, capital letters and nuumber s'''
    if not flag :
        xx, yy = [], [] 
        for i, j in enumerate(msg):
            xx.append(i)
            yy.append(j)
        word_dict = dict(zip(xx, yy))
        #print(f"word dictionary: {word_dict} length: {len(word_dict)}")


    # x = msg.split()
    # print(x)
    

    if not flag:
        '''Key Mapping based on a particular word'''
        key_caps, key_small, key_num = [], [], []
        for key in word_dict:
            #print(f"key: {key} val: {word_dict[key]}")
            ''' Determine the  category of letters here and separate'''
        
            if word_dict[key].isupper():
                key_caps.append(key)
            elif word_dict[key].islower():
                key_small.append(key)
            elif word_dict[key].isdigit():
                key_num.append(key)
        #print(f'keys: \nCaps: {key_caps}\nSmall: {key_small}\ndigit: {key_num} ')
    
        '''Get the  Capital letters from the dict using keys'''
        arr_capital = ''
        for j in key_caps:
            arr_capital += word_dict[j]
        #print(f'arr_capital:{arr_capital}')

        '''Get the small letters from the dict using the keys'''
        arr_small = ''
        for j in key_small:
            arr_small += word_dict[j]
    
        '''Get the Numbers from the dict using the keys'''
        arr_number = ''
        for j in key_num:
            arr_number += word_dict[j]
    
      #  print (f"Caps: {arr_capital}, Small: {arr_small}, Number: {arr_number}")

    else:
        if cp > 0 and sm == 0 and nu == 0:
            arr_capital = msg
            arr_small = ""
            arr_number = ""
        elif cp == 0 and sm > 0 and nu == 0:
            arr_small = msg
            arr_capital = ""
            arr_number = ""
        elif cp == 0 and sm == 0 and nu > 0:
            arr_number = msg
            arr_capital = ""
            arr_small = ""


    '''##################### Main Encryption Process Start here ################### '''

    ''' Capital letters encryption process '''

    if len(arr_capital) > 0:
        cap_x = arr_capital
        # cap_x = 'HELLO'
    else:
        cap_x = ""

    '''TODO For Encrypting Capital letters of length 1 and length 2 '''
    if len(cap_x) > 2:
        as_num = ""
        for j in cap_x:
            ''' Get the letter ascii value and concat it by following next ascii value '''
            as_num += str(ord(j))
        print(f'ascii capital: {as_num}')
        b = int(as_num)
        
    
        '''TODO SOLVE for capital '''

        ''' strbb1 is the return value of number_system_127(b) '''

        enc1, enc2 = "", ""
        
        strbb1 = number_system_127(b)
        getstrbb1 = strbb1[0].split('-')
        # print(f'getstrbb1: {getstrbb1}')
        counter_value = getstrbb1[1] 
        if len(strbb1) > 1:    
            for k in (getstrbb1[0]):
                #print(k)
                #print(chr(65+int(k)))
                enc1 += chr(65+int(k))
            # print(enc1)

            enc1 += str(counter_value)
            print(f'caps enc1: {enc1}')

            # print("----",strbb1)
        
            for k in strbb1[1]:
                enc2 += chr(90 - int(k))
        # print(enc2)

        ''' append the after decimal string in a reverse order'''

        if len(msg).__eq__(1):
            shortMsg = Short_Message(msg)
            enc = shortMsg.encrypt_single_msg()
            print("encrypted text: ", enc)
            return enc
           

        else:
            enc = enc1 + enc2[::-1]
            print("encrypted text: ", enc)
        ''' symmetric key of 1st second array value using xor operation'''
        
        ''' Calculating the secret key simply '''
        xor_strbb1 = [int(getstrbb1[0])] + [int(strbb1[1])]
       # print(f'xor_strbb1: {xor_strbb1}')
        for i in xor_strbb1:
            secret_key_capital ^= int(i)
        print("secret key: ", secret_key_capital)

        # return (enc, secret_key_capital)
        
    else:
        print(colored('Capital word must be of minimum size 3. Due to complexity issue capital word size less than length 3 is not implemented', 'yellow'))

    '''TODO Small Letter Encryption Process  TODO also check for 1 char and 2 char '''   
    
    small_x = arr_small
   # print(f"small_x: {small_x}")
    if len(small_x) > 2:
        call_small_func = small_letters.Small_Letter(small_x)
        #print(f'Small Letter: {call_small_func.encrypt_small_message()}, type: {type(call_small_func.encrypt_small_message())}')
        call_small_func_toInt = int(call_small_func.encrypt_small_message())
        calc_num_127 = number_system_127(call_small_func_toInt)
        ''' Converted to num 127 format using 127 bit number system value and split the decimal value'''
       # print(f'calculate num 127: {calc_num_127}')
        counter_value = calc_num_127[0].split('-')[1]
       # print(f'counter value: {counter_value}')

        ''' For calc_num_127[index1] excluding counter value extract each value and add it to 97 as of ascending order '''

        small_enc1, small_enc2 = "", ""
       # print(f"calc_num_127: {calc_num_127}")
       # print(calc_num_127[0].split('-')[0])
        for k in calc_num_127[0].split('-')[0]:
            small_enc1 += chr(97 + int(k))
        small_enc1 += str(counter_value)
       # print(f'small_enc1: {small_enc1}')

        ''' For calc_num_127[index2] extract each value and subtract it from 122 to be in reverse order '''
        for k in calc_num_127[1]:
            small_enc2 += chr(122 - int(k))
       # print(f'small_enc2: {small_enc2}, sameLength: {len(small_enc2).__eq__(len(calc_num_127[1]))}') 

        ''' Concat the two small_enc generated value such that second small_enc is in reverse order '''
        small_enc = small_enc1 + small_enc2[::-1]
        print(f'encrypted small letters: {small_enc}')

        '''Calculate the key like 53.5 i.e. base127(53) xor base127(5)'''
        
        
        secret_key_small = int(calc_num_127[0].split('-')[0]) ^ int(calc_num_127[1])
        print("secret key small: ", secret_key_small)

        # return (small_enc, secret_key_small)


    else:
        '''TODO return something else if any cause arises '''
        print(colored("The small letter word must of minimum size 3. Due to complexity issue of base127, small letter word length < 3 can't be calculated", 'yellow'))


    '''Numbers Encryption Process '''

    number_x = arr_number
    if len(number_x) > 0:
        print(colored('digits are present', color='green'))
        number_func = number.Number(number_x)
        call_num_func = number_func.encrypt_number()
      #  print(f'call_num_func: {call_num_func}')
         
        ''' For the number encryption
            1. Reverse the acii value of the number
            2. N => Acii is 78
            3. So add each ascii value unit with 78 to generate capital letter in encrypted format  
         '''
        
        rev_num_ascii = call_num_func[::-1]
        num_enc = ''
        for k in rev_num_ascii:
            num_enc += chr(78 + int(k))
        print(f'encrypted number: {num_enc}')


        ''' calculate key but weak in number encryption because the key is the encrypted number '''
        secret_key_num = call_num_func
        print(f"Secret Key Num: {secret_key_num}")


    else:
        print(colored("No numbers included on the word", color="magenta"))

    
    ''' Let the dict key be our public key on order to identify it and it should be the first one to be entered to identify '''

    if not flag:
       # print(f'{key_caps, key_num, key_small}')  
        key_caps_str, key_num_str, key_small_str = '', '', ''
        for i in key_caps:
            key_caps_str += str(i) + "-"
        for i in key_num:
            key_num_str += str(i) + "-"
        for i in key_small:
            key_small_str += str(i) + "-"
       # print(f'cap: {key_caps_str}, num: {key_num_str}, small: {key_small_str} ')  

        ''' Let arrange the keys as in format [Alphabetic Character][Number] where 
            Alphabetic Character : c => Upper Case keys
            Alphabetic Character : n => Number format Keys
            Alphabetic Character : s => Lower case Keys
        '''
        key_caps_str =  'c' + key_caps_str
        key_num_str = 'n' + key_num_str
        key_small_str = 's' + key_small_str

        # print(f'encypted code=> caps: {key_caps_str}, num: {key_num_str}, small: {key_small_str}')

        encrypted_text_order = key_caps_str + key_num_str + key_small_str
        print(f'Encrypted text order mapping: {encrypted_text_order}')
    
        ''' Concat all  the encrypted text in such a way that it is easy to identify whether it is a for Capital, Small or Number '''
        try:
            print(f'encrypted capital: {enc}, encrtpted small: {small_enc}, encrypted number: {num_enc}')
        

            ''' encrypyted text should be concatenated using " - "  '''

            final_encrypt = f'{enc}-{small_enc}-{num_enc}'

            print("Whole encrypted word: {0}".format(final_encrypt))

            ''' Calculate the xor for all the three xor keys using the xor operation '''

            # print(f"secret Keys: secret_key_small: {secret_key_small}, secrret_key_capital: {secret_key_capital}, secret_key_num: {secret_key_num}")
            combined_secret_key = int(secret_key_small) ^ int(secret_key_capital) ^ int(secret_key_num)

            print(f"Combined Secret key: {combined_secret_key}")
            return (final_encrypt, combined_secret_key, encrypted_text_order)
        except:
            print(colored("ERROR: The text must be a combination Capital, Small and numbers and each must have length 3", 'magenta'))
            
           
    
    else:
        print(f'Encrypted text order mapping: {None}')
        encrypted_text_order = None
        
     #   print(f'encrypted cap: {enc}, encrypted number: {num_enc}, encrypted small :{small_enc}')
        
        if len(msg).__eq__(cp):
            return (enc, secret_key_capital, encrypted_text_order)
        elif len(msg).__eq__(sm):
            return (small_enc, secret_key_small, encrypted_text_order)
        elif len(msg).__eq__(nu):
            return (num_enc, secret_key_num, encrypted_text_order)
       
       

# encryptStr()