import math
import small_letters
import number

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
    strbb1 = str(bb1)
    strbb1 = strbb1.split(".")
    #print(strbb1)
    ''' Add the counter at end of index0'''
    strbb1[0] += str(c)
    #print(f'function strbb1: {strbb1}')
    ''' return [(Integer Value index1 + counter value), Integer Value index2] '''
    return strbb1
   


def encryptStr():
    '''# sm_x = small_letters.Small_Letter('halo')
    # y = sm_x.encrypt_small_message()
    # print(y)
'''
    
    # msg = input('enter message: ')
    msg = 'Hello0'
    ''' Use Dict to get the records of small letters, capital letters and nuumber s'''
    xx, yy = [], []
    for i, j in enumerate(msg):
        xx.append(i)
        yy.append(j)
    word_dict = dict(zip(xx, yy))
    print(f"word dictionary: {word_dict} length: {len(word_dict)}")


    # x = msg.split()
    # print(x)
    

    '''Key Mapping based on a particular word'''
    key_caps, key_small, key_num = [], [], []
    for key in word_dict:
        print(f"key: {key} val: {word_dict[key]}")
        ''' Determine the  category of letters here and separate'''
        
        if word_dict[key].isupper():
            key_caps.append(key)
        elif word_dict[key].islower():
            key_small.append(key)
        elif word_dict[key].isdigit():
            key_num.append(key)
    print(f'keys: \nCaps: {key_caps}\nSmall: {key_small}\ndigit: {key_num} ')
    
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
    
    print (f"Caps: {arr_capital}, Small: {arr_small}, Number: {arr_number}")

    '''##################### Main Encryption Process Start here ################### '''

    ''' Capital letters encryption process '''
    
    #cap_x = arr_capital
    cap_x = 'HELLO'
    if len(cap_x) > 0:
        as_num = ""
        for j in cap_x:
            ''' Get the letter ascii value and concat it by following next ascii value '''
            as_num += str(ord(j))
        # print(as_num)
        b = int(as_num)
        
    
        '''TODO SOLVE for capital '''

        ''' strbb1 is the return value of number_system_127(b) '''

        enc1, enc2 = "", ""
        strbb1 = number_system_127(b)
        counter_value = strbb1[0][-1] 
        if len(strbb1) > 1:    
            for k in (strbb1[0][:-1]):
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

        else:
            enc = enc1 + enc2[::-1]
            print("encrypted text: ", enc)
        ''' symmetric key of 1st second array value using xor operation'''
        
        ''' Calculating the secret key simply '''
        key = 0
        for i in strbb1:
            key ^= int(i)
        print("secret key: ", key)
        print(ord('a'), ord('z'))
    else:
        ''' TODO Retrun something else if cause arises'''
        return None 

    '''TODO Small Letter Encryption Process  TODO also check for 1 char and 2 char '''   
    
    small_x = arr_small
    if len(small_x) > 0:
        call_small_func = small_letters.Small_Letter(small_x)
        #print(f'Small Letter: {call_small_func.encrypt_small_message()}, type: {type(call_small_func.encrypt_small_message())}')
        call_small_func_toInt = int(call_small_func.encrypt_small_message())
        calc_num_127 = number_system_127(call_small_func_toInt)
        ''' Converted to num 127 format using 127 bit number system value and split the decimal value'''
        print(f'calculate num 127: {calc_num_127}')
        counter_value = calc_num_127[0][-1]
        print(f'counter value: {counter_value}')

        ''' For calc_num_127[index1] excluding counter value extract each value and add it to 97 as of ascending order '''

        small_enc1, small_enc2 = "", ""
        for k in calc_num_127[0][:-1]:
            small_enc1 += chr(97 + int(k))
        small_enc1 += str(counter_value)
        print(f'small_enc1: {small_enc1}')

        ''' For calc_num_127[index2] extract each value and subtract it from 122 to be in reverse order '''
        for k in calc_num_127[1]:
            small_enc2 += chr(122 - int(k))
        print(f'small_enc2: {small_enc2}, sameLength: {len(small_enc2).__eq__(len(calc_num_127[1]))}') 

        ''' Concat the two small_enc generated value such that second small_enc is in reverse order '''
        small_enc = small_enc1 + small_enc2[::-1]
        print(f'encrypted small letters: {small_enc}')


    else:
        return None


    '''TODO Numbers Encryption Process '''

    number_x = arr_number
    number_x = '12345'
    if len(number_x) > 0:
        number_func = number.Number(number_x)
        call_num_func = number_func.encrypt_number()
        print(f'call_num_func: {call_num_func}')
         
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

    else:
        return None

    
    ''' TODO return the counter or identity in order to decrypt the encrypted text  '''

    ''' TODO return the keys in order to arrange it in original format order '''
    
    ''' Let the dict key be our public key on order to identify it and it should be the first one to be entered to identify '''

    print(f'{key_caps, key_num, key_small}')  
    key_caps_str, key_num_str, key_small_str = '', '', ''
    for i in key_caps:
        key_caps_str += str(i)
    for i in key_num:
        key_num_str += str(i)
    for i in key_small:
        key_small_str += str(i)
    print(f'cap: {key_caps_str}, num: {key_num_str}, small: {key_small_str} ')  

    ''' Let arrange the keys as in format [Alphabetic Character][Number] where 
        Alphabetic Character : c => Upper Case keys
        Alphabetic Character : n => Number format Keys
        Alphabetic Character : s => Lower case Keys
    '''
    key_caps_str =  'c' + key_caps_str
    key_num_str = 'n' + key_num_str
    key_small_str = 's' + key_small_str

   # print(f'encypted code=> caps: {key_caps_str}, num: {key_num_str}, small: {key_small_str}')

    encrypted_key = key_caps_str + key_num_str + key_small_str
    print(f'encrypted public key: {encrypted_key}')
    
    ''' Concat all  the encrypted text in such a way that it is easy to identify whether it is a for Capital, Small or Number '''

    print(f'encrypted capital: {enc}, encrtpted small: {small_enc}, encrypted number: {num_enc}')

    ''' encrypyted text should be concatenated using " - "  '''

    final_encrypt = f'{enc}-{small_enc}-{num_enc}'

    print("Whole encrypted word: {0}".format(final_encrypt))



encryptStr()