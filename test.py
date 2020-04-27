import encryptText
import decryptText


''' Each words makes a sentence'''

def test():
    sentence = "HELLO SANDEEP where have you been and whats YOUR PHONE NUMBER 87094754 code HeL458LonEmjdhf THERE WAS CAT under the BED ofcCOodeE1237 "
    sentence = sentence.split()
    encrypted_sentence, keylist, order,  = [], [], []

    for i in sentence:
        encrypted_texts, secret_keys, text_order = encryptText.encryptStr(i)
        # print(f'encrypted_texts: {encrypted_texts}, secretskeys: {secret_keys}, encrypted_text_order: {text_order}')
        encrypted_sentence.append(encrypted_texts)
        keylist.append(secret_keys)
        order.append(text_order)
   # print(encrypted_sentence, keylist, order)
    print(f'encrypted sentence: \'{" ".join(encrypted_sentence)}\'')


    '''For decrypting each word '''
    decrypted_result = []
    check_decrypt_status = []
    success_count = 0
    for i in range(len(sentence)):
        decrypted_result.append(decryptText.decryptText(encrypted_sentence[i], keylist[i], order[i]))
        if decryptText.decryptText(encrypted_sentence[i], keylist[i], order[i]).__eq__(sentence[i]):
            check_decrypt_status.append("success")
            success_count += 1
        else:
            check_decrypt_status.append("unsuccessful")
    print('\n')
    print("Decrypted Text:")
    print(" ".join(decrypted_result))
    print(" ".join(check_decrypt_status))
    print(f'Decrypting Success rate : {round(((success_count / len(sentence)) * 100), 2)} %')

test()