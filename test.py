import encryptText
import decryptText

''' Each words makes a sentence'''

def test():
    sentence = "HELLO sandeep what isin SAMCABcoffee124"
    sentence = sentence.split()
    encrypted_sentence, keylist, order,  = [], [], []

    for i in sentence:
        encrypted_texts, secret_keys, text_order = encryptText.encryptStr(i)
        # print(f'encrypted_texts: {encrypted_texts}, secretskeys: {secret_keys}, encrypted_text_order: {text_order}')
        encrypted_sentence.append(encrypted_texts)
        keylist.append(secret_keys)
        order.append(text_order)
    print(encrypted_sentence, keylist, order)
    print(f'encrypted sentence: {" ".join(encrypted_sentence)}')

    '''For decrypting each word '''
    decrypted_result = []
    for i in range(len(sentence)):
        decrypted_result.append(decryptText.decryptText(encrypted_sentence[i], keylist[i], order[i]))
    print(" ".join(decrypted_result))
test()