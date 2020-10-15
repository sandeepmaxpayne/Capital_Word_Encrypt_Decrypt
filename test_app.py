import encryptText
import decryptText
from termcolor import colored

''' Each words makes a sentence'''

# Only for testing the whole prgram
def test():
    sentences = "HELLO SANDY where have you been and whats YOUR PHONE NUMBER 1234567890 code HeL458LonEmjdhf THERE WAS CAT under the BED ofcCOodeE1237 This is all about IMAGINATION"
    # sentences = input("Enter sentence:")
    sentences = sentences.rstrip(" ").lstrip(" ").split(" ")
    sentence = []
    for i in sentences:
        if len(i) > 2:
            sentence.append(i)

    encrypted_sentence, keylist, order,  = [], [], []

    for i in sentence:
        if len(i) > 2:
            try:
                encrypted_texts, secret_keys, text_order = encryptText.encryptStr(i)
                # print(f'encrypted_texts: {encrypted_texts}, secretskeys: {secret_keys}, encrypted_text_order: {text_order}')
                encrypted_sentence.append(encrypted_texts)
                keylist.append(secret_keys)
                order.append(text_order)
                # print(encrypted_sentence, keylist, order)
            except:
                print(colored("Unable to fetch the keys. Make sure that word must be a combination of  Capital, Small and number or Single Capital , Small, length words of minimum size 3", color='red'))
        else:
            print(colored("Word length is less than 3, cannot encrypt it", color='red'))

        # print(sentence)
        # print(encrypted_sentence, keylist, order)
    '''For decrypting each word '''
    decrypted_result = []
    check_decrypt_status = []
    success_count = 0

    for i in range(len(sentence)):
        try: 
            decrypted_result.append(decryptText.decryptText(encrypted_sentence[i], keylist[i], order[i]))
        except:
            pass
    for j in decrypted_result:
        if j in sentence:
            check_decrypt_status.append("success")
            success_count += 1
        else:
            check_decrypt_status.append("unsuccessful")
    print()
    print(colored(f'input sentence or word: \'{" ".join(sentences)}\'', color='white', attrs=['underline']))
    print(colored(f'original sentence after loss: \'{" ".join(sentence)}\'', color='yellow', attrs=['underline']))
    print(colored(f'encrypted sentence: \'{" ".join(encrypted_sentence)}\'', color='green', attrs=['underline']))
    print(f'encryption success count: {success_count}')
    print('\n')
    print(colored("Decrypted Text:", attrs=['bold', 'underline']))
    print(" ".join(decrypted_result))
    print(" ".join(check_decrypt_status))
    if round(((success_count / len(sentences)) * 100), 2) > 80.0:
        print(colored(f'Decrypting Success rate : {round(((success_count / len(sentences)) * 100), 2)} %', color='green'))
    elif round(((success_count / len(sentences)) * 100), 2) >= 50.0 and round(((success_count / len(sentence)) * 100), 2) <= 80.0:
        print(colored(f'Decrypting Success rate: {round(((success_count / len(sentences)) * 100), 2)}%', color='cyan'))
    else:
        print(colored(f'Decrypting Success rate: {round(((success_count / len(sentences)) * 100), 2)}%', color='red'))
        



test()
