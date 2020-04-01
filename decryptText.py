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

    complex_encrypted_text = 'CFDC6WRSTQWXVRSXVY-gjd3yssurvurrxvsx-VR'
    separate_complex = complex_encrypted_text.split('-')
    print(f'compex separated: {separate_complex}')

    # small_encrypted_input = 'gjd3yssurvurrxvsx'
    # number_encrypted_input = 'VR'


    for i in separate_complex:
        if i[0].islower():
            small_encrypted_input  = i
        elif i[0].isupper() and re.findall(r'\d', i):
            capital_encrp_text = i
        else:
            number_encrypted_input = i
    
    print(f'cap_encypted: {capital_encrp_text}, small_encrypted: {small_encrypted_input}, number_encrypted: {number_encrypted_input}')
  
   
    ErrRed = lambda x: '\033[31m' + str(x)
 
    ''' suppose 10000 is main key do sub and get pub and priv key, then combine both to get exact to get sol'''
    secret_key = 1427842371713
   # encrp_text = input("Enter the encrypted text: ")
    # capital_encrp_text = 'DFEJ4UYTYSSQWUSXZ'
    #secret_key = int(input("Enter secret key: "))
    iter = re.findall(r'\d', capital_encrp_text)
    x = re.split(r'\d', capital_encrp_text)
    print(x, iter)

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
        #   print(decryp2)

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

    '''TODO Decrypt the small letter encypted text '''

    decrypt_small_text = decryptSmall.DecryptSmallLetter(small_encrypted_input).decrypt_small()
    print(f'decrypted small text: {decrypt_small_text}')

    '''TODO Decrypt the encrypted number  '''

    decrypt_number_str = decrypt_number.Number_decryption(number_encrypted_input).decrypt_number_function()
    print(f'decrypted number:  {decrypt_number_str}')

    '''TODO Arrange the order of all decryoted letter and number using the decrypted order dictionary '''
    
    ''' Get the encrypyted order key dictionary '''
    encrypted_order_key = 'c0123456n11s78910'
    decrypted_order_key_dict = decrypt_order_key.OrderKey(encrypted_order_key).decrypt_order_key()
    print(f'decrypted order key dict: {decrypted_order_key_dict}')
    
    decrypted_capital_txt = txt
    print(f'decrypted capital text: {decrypted_capital_txt}')


    '''Converet the string index "0123" to integer value index '''
    single_digit_c, single_digit_s, single_digit_n = '', '', '' 
    double_digit_c, double_digit_s, double_digit_n = '', '', ''    
    is_nine_c = '9' in decrypted_order_key_dict['c'] 
    is_nine_s = '9' in decrypted_order_key_dict['s']
    is_nine_n = '9' in decrypted_order_key_dict['n']

    token = 0
    
    if is_nine_c.__eq__(True):
        index_nine = decrypted_order_key_dict['c'].index('9')
        single_digit_c = decrypted_order_key_dict['c'][:index_nine+1]
        double_digit_c = decrypted_order_key_dict['c'][index_nine+1:]
        token += 1
    else:
        single_digit_c = decrypted_order_key_dict['c'][:]

    if token == 1:
        double_digit_s = decrypted_order_key_dict['s'][:]
        token += 1
    elif is_nine_s.__eq__(True):
        index_nine = decrypted_order_key_dict['s'].index('9')
        single_digit_s = decrypted_order_key_dict['s'][:index_nine+1]
        double_digit_s = decrypted_order_key_dict['s'][index_nine+1:]
        token += 1
    else:
        single_digit_s = decrypted_order_key_dict['s'][:]

    if token >=1:
        double_digit_n = decrypted_order_key_dict['n'][:] 
    elif is_nine_n.__eq__(True):
        index_nine = decrypted_order_key_dict['n'].index('9')
        single_digit_n = decrypted_order_key_dict['n'][:index_nine+1]
        double_digit_n = decrypted_order_key_dict['n'][index_nine+1:]
    else:
        single_digit_n = decrypted_order_key_dict['n'][:]
    #print(f'single c: {single_digit_c}, double c: {double_digit_c}\nsingle s: {single_digit_s}, double s: {double_digit_s}\nsingle n: {single_digit_n}, double n: {double_digit_n}')

    single_digit, double_digit = '', ''

    single_digit = single_digit_c + single_digit_s + single_digit_n
    double_digit = double_digit_c + double_digit_s + double_digit_n

    print(f'singledigitL {single_digit}, doubledigit: {double_digit}')

    single_dig_list = re.findall(r'\d{1}', single_digit)
    double_dig_list = re.findall(r'\d{2}', double_digit)
    print(f'single_dig_list: {single_dig_list}, double_dig_list: {double_dig_list}')    


decryptText()